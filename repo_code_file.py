import json
import os
from datetime import datetime

file_path = 'patient_data.json'
# file_path = 'test_patient_info.json'

# This code generates unique IDs for the patients information
def generating_patient_ids(data):
    """This program generates patient IDs based on the number of keys in the json file"""
    return(len(data)+1)

def creating_patient_info(file_path=file_path):
    """This function creates a dictionary of a patients basic information.
    Parameters: 
    file_path -> Name of the json file.
    BloodPressure -> Starting all blood pressure values at 0.
    """

    collectibles = ['Name(First and Last Name)', 'Gender', 'YearofBirth(DD-MM-YYYY)', 'Location']
    data_dict = {}
    print("Please provide the required information")
    for i in collectibles:
            while True:  # Loop until valid input is provided
                user_input = input(f"What is your {i}: ")
                
                if i == 'YearofBirth(DD-MM-YYYY)':
                    try:
                        birth_date = datetime.strptime(user_input, "%d-%m-%Y")
                        data_dict[i] = birth_date.strftime("%d-%m-%Y")  # Save the valid date input
                        # Calculate age
                        today = datetime.today()
                        data_dict['Age'] = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month,birth_date.day))
                        break  # Exit the loop on valid input
                    except ValueError:
                        print("Invalid date format! Please use the DD-MM-YYYY format.")
                elif i == 'age':
                    data_dict[i] = data_dict['YearofBirth(YYYY-MM-DD)']
                        
                else:
                    if user_input.strip():  # Ensure input is not empty
                        data_dict[i] = user_input.lower()  # Store input and convert to lowercase
                        break  # Exit loop on valid input
                    else:
                        print(f"{i} cannot be empty. Please enter a value.")

    # Create id. If the size of the json file is 0, the loaded data comes empty
    # Load or initialize JSON data
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path) as f:
            loaded_data = json.load(f)
    else:
        loaded_data = {}
            
    id_number = generating_patient_ids(loaded_data)

    # Add the collected data to the loaded data
    loaded_data[id_number] = data_dict
    return loaded_data

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
        
# Add other columns
def gettingpatientdata(file_path=file_path):
    with open(file_path) as f:
        data = json.load(f)
    
    key_searched = input("Patient ID: ")
    patient_found = False

    for key, values in data.items():
        if key == key_searched:
            print(values)  # Open the dashboard with the patient's information
            patient_found = True
            break  # Exit the loop if the patient is found
    
    if not patient_found:
        print("Patient has no such data. Collecting data...")
        saving_data()

def appointmentdate_data(file_path=file_path):
    with open(file_path) as f:
        data = json.load(f)
    
    key_searched = input("Patient ID: ")
    patient_found = False  # Flag to track if the patient ID was found

    for key, values in data.items():
        if key == key_searched:
            patient_found = True
            # Initialize 'Previous Appointment' if it doesn't exist
            if 'Previous Appointment' not in values:
                values['Previous Appointment'] = None
            else:
                # Set 'Previous Appointment' to current 'Next Appointment'
                values['Previous Appointment'] = values['Next Appointment']
                
            # Prompt the user to input the next appointment date
            while True:
                try:
                    next_appointment_str = input("Add the next appointment (format DD-MM-YYYY): ")
                    next_appointment = datetime.strptime(next_appointment_str, "%d-%m-%Y").date()
                    values['Next Appointment'] = next_appointment.strftime("%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid format. Please enter the date in the format DD-MM-YYYY")
                    
            print(f"Updated appointment details for patient id - {key}.")
            
            # Save the updated data
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            break  # Exit the loop once the patient data is updated

    # If the patient ID was not found, display the message once
    if not patient_found:
        print("Patient has no such data. Collecting data...")
        saving_data()  # Call to save new data if needed

# Adding Blood Pressure values for the past 5 visits.
def blood_pressure_adjustments(file_path=file_path):
    with open(file_path) as f:
        data = json.load(f)
        
    key_searched = input("Patient ID: ")
    patient_found = False  # Flag to track if the patient ID was found
    for key, values in data.items():
        if key == key_searched:
            patient_found = True
            # Initialize 'BloodPressure-1' if it doesn't exist
            # A list of allowed blood pressure values
            bp_keys = ['Blood Pressure 1', 'Blood Pressure 2', 'Blood Pressure 3', 'Blood Pressure 4', 'Blood Pressure 5']
            # Check if we need to create new blood pressure entries or shift existing ones
            for i, bp_key in enumerate(bp_keys):
                # If the blood pressure key doesn't exist, prompt for a new value and add it
                if bp_key not in values:
                    values[bp_key] = int(input(f"Enter value for {bp_key}: "))
                    print(f"Added new entry: {bp_key} with value {values[bp_key]}")
                    break  # Stop the loop once we've added a new entry
                
                # If we reach the last blood pressure key and it exists, shift values
                if i == len(bp_keys) - 1:
                    # Shift the values down from Blood Pressure 4 to Blood Pressure 1
                    for j in range(len(bp_keys) - 1):
                        values[bp_keys[j]] = values[bp_keys[j + 1]]
                    
                    # Prompt for a new value for Blood Pressure 5
                    values['Blood Pressure 5'] = int(input(f"Enter new blood pressure value for {bp_keys[-1]}: "))
                    print("Shifted existing blood pressure values and added new value for Blood Pressure 5")
            
            # Save the updated data
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            
            print(f"Updated Blood Pressure details for patient ID {key}.")
            break  # Exit the loop once the patient data is updated
    
    # If the patient ID was not found, display the message once
    if not patient_found:
        print("Patient has no such data. Collecting data...")
        saving_data()  # Call to save new data if needed