document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const inputTemperature = document.getElementById('inputTemperature').value;
    const inputHumidity = document.getElementById('inputHumidity').value;
    const inputRainfall = document.getElementById('inputRainfall').value;

    // Send POST request to Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            input_features: [inputTemperature, inputHumidity, inputRainfall]
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display the predicted value
        document.getElementById('predictionResult').innerHTML = `Crop: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
