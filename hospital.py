class Hospital:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.bed_number = len(self.patients)
            print(f"Patient {patient.id} admitted to {self.name}")
        else:
            print(f"Sorry, {self.name} is full")
        return self

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                patient.bed_number = None
                print(f"Patient {patient.id} discharged from {self.name}")
                return self
        print(f"Patient with ID {patient_id} not found in {self.name}")
        return self

