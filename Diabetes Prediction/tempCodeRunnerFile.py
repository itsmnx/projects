from flask import Flask, render_template, request, jsonify
import csv
import os
from d import predict_diabetes


app = Flask(__name__)
HISTORY_FILE = 'patient_history.csv'

def save_patient_history(input_data, diagnosis):
    file_exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Diagnosis'])
        writer.writerow(input_data + [diagnosis])

def load_patient_history():
    if not os.path.isfile(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

@app.route('/')
def index():
    performance_metrics = {
        'accuracy': 0.92,
        'precision': 0.89,
        'recall': 0.90,
        'f1_score': 0.895
    }
    return render_template('index.html', metrics=performance_metrics)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [
            float(request.json['Pregnancies']),
            float(request.json['Glucose']),
            float(request.json['BloodPressure']),
            float(request.json['SkinThickness']),
            float(request.json['Insulin']),
            float(request.json['BMI']),
            float(request.json['DiabetesPedigreeFunction']),
            float(request.json['Age'])
        ]
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input values'}), 400

    prediction = predict_diabetes(input_data)
    diagnosis = 'Diabetic' if prediction == 1 else 'Not Diabetic'
    save_patient_history(input_data, diagnosis)
    return jsonify({'diagnosis': diagnosis})

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/api/history')
def api_history():
    return jsonify(load_patient_history())

if __name__ == '__main__':
    app.run(debug=True)
