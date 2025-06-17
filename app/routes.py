from flask import Blueprint, render_template, request
from app.utils.predict import predict_heart_attack

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            features = [
                float(request.form.get('age')),
                float(request.form.get('sex')),
                float(request.form.get('cp')),
                float(request.form.get('trestbps')),
                float(request.form.get('chol')),
                float(request.form.get('fbs')),
                float(request.form.get('restecg')),
                float(request.form.get('thalach')),
                float(request.form.get('exang')),
                float(request.form.get('oldpeak')),
                float(request.form.get('slope')),
                float(request.form.get('ca')),
                float(request.form.get('thal'))
            ]
            prediction = predict_heart_attack(features)
        except Exception as e:
            prediction = f"Error: {e}"
    
    return render_template('index.html', prediction=prediction)
# Flask routes will go here
