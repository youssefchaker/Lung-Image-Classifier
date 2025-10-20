# Lung Image Classifier

This is a web application that uses a deep learning model to classify lung X-ray images into three categories: COVID, NORMAL, and PNEUMONIA.

## Features

*   **Prediction:** Upload a lung X-ray image and get a prediction from a trained model.
*   **Multiple Models:** The application supports different deep learning models:
    *   A custom Convolutional Neural Network (CNN)
    *   DenseNet
    *   GoogleNet
*   **Training:** The ability to retrain the models using the provided training scripts.
*   **Web Interface:** A user-friendly web interface for uploading images and viewing results.

## Folder Structure

```
├── app.py                      # Main Flask application
├── Custom_model_training.py    # Script to train the custom CNN model
├── Dense_model_training.py     # Script to train the DenseNet model
├── Googlenet_model_training.py # Script to train the GoogleNet model
├── utils.py                    # Utility functions for data processing
├── datasets/
│   ├── Models/                 # Saved trained models
│   ├── test/                   # Test images
│   └── train/                  # Training images
├── templates/
│   └── presentation.html       # Main HTML template for the web interface
├── static/                     # Static files (CSS, JS, images)
└── README.md                   # This file
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Lung-Image-Classifier
    ```

2.  **Install dependencies:**
    It is recommended to create a virtual environment.
    ```bash
    pip install Flask tensorflow Pillow numpy
    ```
    Or create a `requirements.txt` file with the following content and run `pip install -r requirements.txt`:
    ```
    Flask
    tensorflow
    Pillow
    numpy
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

2.  **Make a prediction:**
    *   Open your web browser and navigate to the application's URL.
    *   Choose a model from the dropdown menu.
    *   Click "Choose File" to upload a lung X-ray image.
    *   The prediction results will be displayed on the page.

## Training

To train a model, run the corresponding training script:

*   **Custom Model:**
    ```bash
    python Custom_model_training.py
    ```
*   **DenseNet Model:**
    ```bash
    python Dense_model_training.py
    ```
*   **GoogleNet Model:**
    ```bash
    python Googlenet_model_training.py
    ```

The trained models will be saved in the `datasets/Models/` directory.

## Technologies Used

*   **Backend:** Python, Flask
*   **Machine Learning:** TensorFlow, Keras
*   **Frontend:** HTML, CSS, JavaScript
