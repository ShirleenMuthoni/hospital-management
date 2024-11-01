class Doctor:
    def __init__(self, name, age, gender, specialization, doctor_id):
        # Attributes
        self.name = name
        self.age = age
        self.gender = gender
        self.specialization = specialization
        self.id = doctor_id  # Unique identifier for the doctors

         # Method to display doctor's information
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Gender:", self.gender)
        print("ID:", self.id)  # Instance of a doctor

        # Main guard to create an instance of Doctor
if __name__ == "__main__":  # Corrected the main guard
    doc1 = Doctor("Dr. Olive", 40, "Female", "Pediatrician", 101)
    doc1.display()  # Output: Name: Dr. Olive, Age: 40, Specialization: Pediatrician, Gender: Female, ID: 101
