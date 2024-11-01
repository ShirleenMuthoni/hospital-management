class Appointments:
    def __init__(self):  
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):  
        return self.appointments

    def get_appointment(self, id):
        for appointment in self.appointments:
            if appointment.id == id:
                return appointment  
        return None
    def remove_appointment(self, id):
        for appointment in self.appointments:
            if appointment.id == id:
                self.appointments.remove(appointment)
                return True
        return False
