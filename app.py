from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the dataset
crop_data = pd.read_csv('Crop_recommendation.csv')

# Keep only the selected features and the target variable
selected_features = ['temperature', 'humidity', 'rainfall', 'label']
crop_data = crop_data[selected_features]

# Prepare the data
X = crop_data.drop(['label'], axis=1)
Y = crop_data['label']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Train the model
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, Y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_features = data['input_features']  

    # Convert input to a format that your model expects
    input_array = np.array(input_features).reshape(1, -1)

    # Use the loaded model to make predictions
    prediction = classifier.predict(input_array)

    # Return the prediction as JSON to the frontend
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
