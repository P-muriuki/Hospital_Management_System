import json
import os
from datetime import datetime

file_path = 'patient_data.json'

# This code generates unique IDs for the patients information
def generating_patient_ids(data):
    """This program generates patient IDs based on the number of keys in the json file"""
    return(len(data)+1)

def creating_patient_info(file_path, BloodPressure = 0):
    """This function creates a dictionary of a patients basic information. Then it stores it in a json file.
    Parameters: 
    file_path -> Name of the json file.
    BloodPressure -> Starting all blood pressure values at 0.
    """

    collectibles = ['Name', 'Age', 'Location', 'Gender', 'YearofBirth(YYYY-MM-DD)']
    # 'IDNumber', 'AppointmentDate', 'Weight', 'BloodPressure'
    data_dict = {}
    print("Please provide the required information")
    for i in collectibles:
        user_input = input(f"What is your {i}")
        
        # If i is YearofBirth change type to dateformat
        if i == 'YearofBirth(YYYY-MM-DD)':
            user_input = user_input
            try:
                user_input = datetime.strptime(user_input, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Please use the YYYY-MM-DD format")
                user_input = input(f"What is your {i}")
            data_dict[i]= user_input
        
        else:
            data_dict[i]= user_input
    data_dict['BloodPressure']= BloodPressure
    if all(data_dict.values()):
        # Adjust the string values to lowercase for uniformity
        data_dict = {key: value.lower() if isinstance(value, str) else value for key, value in data_dict.items()}

        # Create id. If the size of the json file is 0, the loaded data comes empty
        if os.path.getsize(file_path) == 0:
            loaded_data = {}
            
        else:
            with open(file_path) as f:
                loaded_data = json.load(f)
                
        id_number = generating_patient_ids(loaded_data)

        # Add the collected data to the loaded data
        loaded_data[id_number] = data_dict
        return loaded_data
    else:
        print("Incomplete information provided!")
        return {}


def saving_data():
    """This program only saves patient information that has values."""
    loaded_data = creating_patient_info(file_path=file_path)
    if loaded_data:
        # Save the data back to the json file
        with open(file_path, 'w') as f:
            json.dump(loaded_data,f, indent=4)
        print("Data has been saved successfully!")
    else:
        print("No data to save; patient information is empty.")