import csv
import random

# Number of records to generate
num_records = 500

# CSV file name
filename = 'patient_history.csv'

# Function to generate a random patient record
def generate_patient_record():
    Pregnancies = random.randint(0, 15)
    Glucose = random.randint(70, 200)
    BloodPressure = random.randint(40, 100)
    SkinThickness = random.randint(10, 50)
    Insulin = random.randint(15, 276)
    BMI = round(random.uniform(15.0, 50.0), 1)
    DiabetesPedigreeFunction = round(random.uniform(0.05, 2.5), 3)
    Age = random.randint(21, 80)

    # Simple rule for diagnosis (just for synthetic data)
    # High glucose or BMI or age increases diabetes risk
    risk_score = 0
    if Glucose > 140:
        risk_score += 2
    if BMI > 30:
        risk_score += 2
    if Age > 45:
        risk_score += 1
    if DiabetesPedigreeFunction > 1.0:
        risk_score += 1

    Diagnosis = 'Diabetic' if risk_score >= 3 else 'Not Diabetic'

    return [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Diagnosis]

# Write CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Diagnosis'])
    # Write data rows
    for _ in range(num_records):
        writer.writerow(generate_patient_record())

print(f"{num_records} patient records saved to '{filename}'")
