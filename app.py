from flask import Flask, render_template, request
import numpy as np
import joblib  # safer than pickle

app = Flask(__name__)

# Load model
model = joblib.load(r"C:\Users\USER\Downloads\Heart Attack Prediction\saved_models\Support Vector Machine.pkl")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract data from form
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            cp = int(request.form['cp'])
            trestbps = int(request.form['trestbps'])
            chol = int(request.form['chol'])
            fbs = int(request.form['fbs'])
            restecg = int(request.form['restecg'])
            thalach = int(request.form['thalach'])
            exang = int(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = int(request.form['slope'])

            # Make prediction
            features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]])
            prediction = model.predict(features)

            result = "High Risk of Heart Attack" if prediction[0] == 1 else "Low Risk of Heart Attack"

            return render_template('index.html', prediction=result)
        except Exception as e:
            return render_template('index.html', prediction=f"Error occurred: {str(e)}")
