import json
from SearchAndUpdateHistory import patient_record
from PatientRegistration import patient_registration
from ViewPatientHistory import viewHistory
from linkup import patients
import uuid


def save_patients(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii= False, indent=2)

def load_patients():
    try:
        with open("HospitalPatientRecords.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    patient_id = str(uuid.uuid4())
    ful_name = input('Please Enter Full Name: ')
    age = int(input('Please Enter Your Age: '))
    print(patient_registration(ful_name, patient_id, age))

    patient_id = str(input('Please Enter Patient ID: '))
    add_note = input('Note: ')
    patient_record(patient_id, add_note)

    pat_ID = input("Enter Patient ID: ").strip()
    viewHistory(pat_ID)


    save_patients(patients, "HospitalPatientRecords.json")
