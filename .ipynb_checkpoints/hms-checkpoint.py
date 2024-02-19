from datetime import date

class BaseSystem:
    """Base class with common functionality"""
    
    def __init__(self, filename):
        self.filename = filename
        self.username = None

    def collect_username(self):
        """Collects the username to be used in many instances"""
        self.username = input("Please provide your full name (first and last name): ")
        self.username = self.username.lower()
        with open('current_patient.txt', 'w') as fn:
            fn.write(self.username)
            
    def getting_username(self, user = ''):
        with open('current_patient.txt','r')as fn:
            self.user = fn.read().strip()
            return self.user

userdictionary = {}
class System(BaseSystem):
    
    def __init__(self, filename):
        super().__init__(filename)
        self.filename = filename
        self.name = None
        self.blood_group = None
        self.location = None
        self.gender = None
        self.year_of_birth = 0
        self.appointment_date = date.today()
        self.weight = 0
        self.blood_pressure = 0
        self.getting_username()
        
    def collect_info(self):
        """This program creates unique Sequential Identification and collects the user info"""
        userdictionary = {}
        information = ["name(first and last)", "blood_group", "location", "gender", "year_of_birth", "weight" ,"blood_pressure"]
        print("Input the required information")
        for info in information:
            if info.title() == "Year_Of_Birth" or info.title() == "Weight" or info.title() == "Blood_Pressure":
                while True:
                    try:
                        uservalue = input(f"Your {info.title()}: ")
                        userdictionary[info] = float(uservalue)
                        break
                    except ValueError:
                        print("Please provide values for this input")
            else:
                uservalue = input(f"Your {info.title()}: ")
                uservalue = uservalue.lower()
                userdictionary[info] = uservalue
        
        with open(filename, "a") as fn:
            fn.write(f"{userdictionary}\n")
    def show_and_find_info(self):
        """Uses a patient's name to search for the rest of the patient's information. 
        If it doesn't exist, prompt user information collection"""
        print(f"Searching for user: {self.user}")
        with open(self.filename) as fn:
            data = fn.readlines()
            for line in data:
                if self.user in line:
                    print("Patient information retrieved!")
                    user1 = eval(line.rstrip())
                    for key, values in user1.items():
                        print(f"{key.title()}:{values}")
                    break
            else:
                print(f"Patient {self.user} not found. Starting data collection...")
                self.collect_info()