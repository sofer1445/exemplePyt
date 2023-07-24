class Patient:
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.doctor = None
        self.nurse = None

    def display_info(self):
        print(f"Patient ID: {self.id}")
        print(f"Patient Name: {self.name}")
        print(f"Patient Allergies: {self.allergies}")
        print(f"Patient Bed Number: {self.bed_number}")
        return self

    def __str__(self):
        return f"Patient ID: {self.id}\nPatient Name: {self.name}\nPatient Allergies: {self.allergies}\nPatient Bed Number: {self.bed_number}"

    def __repr__(self):
        return f"Patient({self.id}, {self.name}, {self.allergies}, {self.bed_number})"

    def finsh_treatment(self, hospital):
        hospital.discharge(self.id)
        return self

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.allergies == other.allergies and self.bed_number == other.bed_number

    def __hash__(self):
        return hash((self.id, self.name, self.allergies, self.bed_number))

    def assign_doctor(self, doctor):
        self.doctor = doctor
        return self

    def assign_nurse(self, nurse):
        self.nurse = nurse
        return self

    def get_doctor(self):
        return self.doctor

    def get_nurse(self):
        return self.nurse

    def discharge(self, hospital):
        hospital.discharge(self.id)
        return self
