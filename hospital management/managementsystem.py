class Patient:
    def __init__(self, name: str, age: int, patient_id: int):
        self.name = name
        self.age = age
        self.patient_id = patient_id

    def display_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"


class Doctor:
    def __init__(self, name: str, age: int, specialization: str):
        self.name = name
        self.age = age
        self.specialization = specialization

    def get_name(self):
        return self.name

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Specialization: {self.specialization}"


class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date: str):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display_info(self):
        return f"Appointment on {self.date} with Dr. {self.doctor.name} for {self.patient.name}"


class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, name: str, age: int, patient_id: int):
        patient = Patient(name, age, patient_id)
        self.patients.append(patient)
        print(f"Added patient: {patient.display_info()}")

    def add_doctor(self, name: str, age: int, specialization: str):
        doctor = Doctor(name, age, specialization)
        self.doctors.append(doctor)
        print(f"Added doctor: {doctor.display_info()}")

    def create_appointment(self, patient_id: int, doctor_name: str, date: str):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.get_name() == doctor_name), None)
        if patient and doctor:
            appointment = Appointment(patient, doctor, date)
            self.appointments.append(appointment)
            print(f"Created appointment: {appointment.display_info()}")
        else:
            print("Error: Patient or Doctor not found!")

    def display_patients(self):
        print("Patients:")
        for patient in self.patients:
            print(patient.display_info())

    def display_doctors(self):
        print("Doctors:")
        for doctor in self.doctors:
            print(doctor.display_info())

    def display_appointments(self):
        print("Appointments:")
        for appointment in self.appointments:
            print(appointment.display_info())


# Sample interaction
if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()

    # Adding patients
    hospital_system.add_patient("Alice", 35, 1)
    hospital_system.add_patient("Rob", 20, 2)

    # Adding doctors
    hospital_system.add_doctor("Dr. Sam", 50, "Cardiology")
    hospital_system.add_doctor("Dr. Lucy", 45, "Gynacology")

    # Creating appointments
    hospital_system.create_appointment(1, "Dr. Sam", "2024-11-01")
    hospital_system.create_appointment(2, "Dr. Lucy", "2024-11-02")

    # Displaying records
    hospital_system.display_patients()
    hospital_system.display_doctors()
    hospital_system.display_appointments()
                               
