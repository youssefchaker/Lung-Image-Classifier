from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import subprocess

app = Flask(__name__, template_folder='templates')

# Flag to indicate training status
training_status = {'status': 'idle'}

def preprocess_image(img):
    # Convert the image to grayscale
    img = img.convert("L")
    
    # Resize the image to (232, 232)
    img = img.resize((232, 232))

    # Convert the image to an array
    img_array = image.img_to_array(img)

    # Expand the dimensions to match the model's input shape
    img_array = np.expand_dims(img_array, axis=0)

    # Normalize the pixel values
    img_array = img_array / 255.0

    # Add an extra dimension for grayscale channel
    img_array = np.expand_dims(img_array, axis=-1)

    return img_array

def decode_predictions(predictions):
    classes = ['COVID', 'NORMAL', 'PNEUMONIA']
    decoded_preds = {}
    for i, pred in enumerate(predictions[0]):
        decoded_preds[classes[i]] = float((pred)*100)
    return decoded_preds

def train_model():
    global training_status
    training_status['status'] = 'training'

    # Execute the train.py script using subprocess
    try:
        subprocess.run(['python', 'train.py'], check=True)
    except subprocess.CalledProcessError as e:
        print('Error during training:', e)
    
    training_status['status'] = 'idle'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image and model choice from the request
        img = Image.open(request.files['image'].stream).convert("RGB")
        model_choice = request.form.get('model_choice', 'model')  # Default to model1 if not provided

        # Load the selected model
        model_path = f'{model_choice}.h5'
        model = load_model(model_path)

        # Preprocess the image
        preprocessed_img = preprocess_image(img)

        # Make a prediction
        predictions = model.predict(preprocessed_img)

        # Decode predictions to readable form
        decoded_predictions = decode_predictions(predictions)

        # Return the predictions
        return jsonify({'predictions': decoded_predictions})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/train', methods=['POST'])
def train():
    global training_status
    if training_status['status'] == 'idle':
        # Start training
        train_model()
        return jsonify({'success': True, 'message': 'Training completed.'})
    else:
        return jsonify({'success': False, 'message': 'Training in progress.'})

@app.route('/training_status', methods=['GET'])
def get_training_status():
    global training_status
    return jsonify(training_status)

if __name__ == '__main__':
    app.run(debug=True)
