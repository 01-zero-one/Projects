from linkup import patients

def patient_registration(full_name, uniq_id, age, history = None):
    if history is None:
        history = []

    user = next((u for u in patients if u["unique_id"] == uniq_id), None)

    if not user:
        patients.append(dict(name=full_name, unique_id=uniq_id, age=age, history=history))
        print(full_name, 'Registration was a success')
    else:
        print(full_name, 'Registration failed due to user already in system.')

    return patients


