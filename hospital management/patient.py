class Patient:
    def __init__(self, name, age, patient_id):
        # Attributes
        self.name = name
        self.age = age
        self.patient_id = patient_id  # Unique identifier
        self.medical_history = []
        # Method to display patient's information
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.patient_id)
  
    # Method to add medical history
    def add_medical_history(self, record):
        self.medical_history.append(record)
         # Method to get medical history
    def get_medical_history(self):
        return self.medical_history

# Instance of a patient
if __name__ == "__main__":  # Corrected the main guard
    pat1 = Patient("Hellen", 20, 1)
    pat1.display()  # Output: Name: Hellen, Age: 20, ID: 1
    # Add medical history
    pat1.add_medical_history("Allergy: red meat")
    
    print("Medical History:", pat1.get_medical_history())

   

   