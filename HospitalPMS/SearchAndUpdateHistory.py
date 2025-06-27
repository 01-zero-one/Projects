from linkup import patients

import datetime

def patient_record(patient_id, add_note):
    match = next((u for u in patients if u['unique_id'] == patient_id), None)

    if match:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        match['history'].append({"note": add_note, "timestamp": timestamp})
        print(f"Note added to {match['name']}'s history.")
        print(match)
    else:
        print("Patient not found.")

# Example usage

