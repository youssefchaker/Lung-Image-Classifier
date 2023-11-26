function previewImage() {
    const input = document.getElementById('imageInput');
    const preview = document.getElementById('imagePreview');

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.innerHTML = `<img src="${e.target.result}" alt="Selected Image" style="max-width:100%;">`;
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function predict() {
    const input = document.getElementById('imageInput');
    const file = input.files[0];

    const formData = new FormData();
    formData.append('image', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const predictionsDiv = document.getElementById('predictions');
        predictionsDiv.innerHTML = '<h3>Predictions:</h3>';
        for (const [classLabel, probability] of Object.entries(data.predictions)) {
            predictionsDiv.innerHTML += `<p>${classLabel}: ${parseInt((probability))+"%"}</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
}
