# app.py
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import os
from PIL import Image

app = Flask(__name__, template_folder='templates')

# Load the model from the same directory as app.py
model_path = 'model.h5'
model = load_model(model_path)



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

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image from the request
        img = Image.open(request.files['image'].stream).convert("RGB")

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

if __name__ == '__main__':
    app.run(debug=True)