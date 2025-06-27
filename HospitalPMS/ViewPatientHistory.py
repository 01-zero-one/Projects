from linkup import patients

def viewHistory(patient_id):
    match = next((u for u in patients if u["unique_id"] == patient_id), None)

    if match:
        if len(match["history"]) > 0:
            print(f'Medical History for {match["name"]} (ID: {match["unique_id"]})')
            for i, x in enumerate(match["history"], start=1):
                print(f'{i}. {[x["timestamp"]]} {x["note"]}')
        else:
            print('No Medical History')
    else:
        print('Patient Not Found')







