# Utility functions will go here
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), r'C:\Users\USER\Downloads\Heart Attack Prediction\saved_models\Support Vector Machine.pkl')

model = joblib.load(model_path)

def predict_heart_attack(features):
    prediction = model.predict([features])[0]
    return 'High Risk' if prediction == 1 else 'Low Risk'

