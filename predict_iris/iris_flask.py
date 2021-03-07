# =============================================================================
# Import Packages
# =============================================================================

import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# =============================================================================
# Load Models
# =============================================================================

# MinMaxScaler
scaler = pickle.load(open('MinMaxScaler.pkl', 'rb'))

# Machine Learning Model
model = pickle.load(open('iris_model_scaled.pkl', 'rb'))

# =============================================================================
# Flask - WebAPI
# =============================================================================

# Initialise Flask
app = Flask(__name__)

# setting HTML template
@app.route('/')
def home():
    return render_template('index.html')

# predicts page
@app.route('/predict', methods = ['POST']) # modify/update the information
def predict():
    features = [np.array([float(x) for x in request.form.values()])] # returning features as float values in a list
    final_features = scaler.transform(features) # features in an array for prediction

    prediction = model.predict(final_features) # using the model to predict

    output = prediction[0] # get string from array

    return render_template('index.html', prediction_text = 'The iris species is {}'.format(output)) # showing output

# results page for request.py
@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True) # obtaining requested data
    prediction = model.predict(scaler.transform([np.array(list(data.values()))])) # using the model to predict

    output = prediction[0] # get string

    return jsonify(output) # format output

# server clause
if __name__ == "__main__":
    app.run(debug=True)
