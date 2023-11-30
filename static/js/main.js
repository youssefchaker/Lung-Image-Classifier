function previewImage() {
    const input = document.getElementById('imageInput');
    const errorMessages = document.getElementById('errorMessages');
    const preview = document.getElementById('imagePreview');

    errorMessages.innerHTML = ''; 

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.innerHTML = `<img src="${e.target.result}" alt="Selected Image" style="max-width:100%;">`;
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function trainModel() {
    const errorMessages = document.getElementById('errorMessages');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const predictionsDiv = document.getElementById('predictions');
    predictionsDiv.innerHTML = '';
    errorMessages.innerHTML = '';

    // Get the selected model from the dropdown
    const selectedModel = document.getElementById('modelSelect').value;

    // Show loading spinner
    loadingSpinner.style.display = 'block';

    // Disable buttons during training
    document.getElementById('predictButton').disabled = true;
    document.getElementById('trainButton').disabled = true;

    // Fetch to the '/train' route with the selected model
    fetch('/train', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ model_choice: selectedModel }),  // Pass the selected model
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            errorMessages.innerHTML = `<p style="color: red;">Error: ${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessages.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    })
    .finally(() => {
        // Hide loading spinner and enable buttons
        loadingSpinner.style.display = 'none';
        document.getElementById('predictButton').disabled = false;
        document.getElementById('trainButton').disabled = false;
    });
}


function predict() {
    const input = document.getElementById('imageInput');
    const file = input.files[0];
    const errorMessages = document.getElementById('errorMessages');
    const modelChoice = document.getElementById('modelSelect').value;

    errorMessages.innerHTML = '';

    if (!file) {
        errorMessages.innerHTML = '<p style="color: red;">Please choose an image.</p>';
        return;
    }

    const formData = new FormData();
    formData.append('image', file);
    formData.append('model_choice', modelChoice);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        const predictionsDiv = document.getElementById('predictions');
        predictionsDiv.innerHTML = '<h3>Predictions:</h3>';
        for (const [classLabel, probability] of Object.entries(data.predictions)) {
            predictionsDiv.innerHTML += `<p>${classLabel}: ${parseInt((probability))+"%"}</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
}



function disableButtons() {
    const predictButton = document.getElementById('predictButton');
    const trainButton = document.getElementById('trainButton');
    
    predictButton.disabled = true;
    trainButton.disabled = true;
}

function enableButtons() {
    const predictButton = document.getElementById('predictButton');
    const trainButton = document.getElementById('trainButton');
    
    predictButton.disabled = false;
    trainButton.disabled = false;
}
