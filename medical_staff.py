# It is a parent department of the entire medical team

class Medical_Staff:
    def __init__(self, name, position, age, salary):
        self.name = name
        self.position = position
        self.age = age
        self.salary = salary
        self.patients = []
        self.rooms = []
        self.beds = []
        self.patients_in_room = []
        self.patients_in_bed = []
        self.rooms_in_patient = []
        self.beds_in_patient = []
        self.num_of_medical_staff = 0


def add_medical_staff(self, name, position, specialty):
    self.name = name
    self.position = position
    self.specialty = specialty
    self.num_of_medical_staff += 1


def edit_medical_staff(self, name, position, specialty):
    self.name = name
    self.position = position
    self.specialty = specialty


def delete_medical_staff(self):
    self.num_of_medical_staff -= 1


def get_information_about_medical_staff(medical_staff):
    return medical_staff.name, medical_staff.position, medical_staff.specialty


def to_string(medical_staff):
    return f"Name: {medical_staff.name}\nPosition: {medical_staff.position}\nSpecialty: {medical_staff.specialty}"


def __eq__(self, other):
    return self.name == other.name and self.age == other.age and self.salary == other.salary and self.department == other.department


def __hash__(self):
    return hash((self.name, self.age, self.salary, self.department))


def __add__(self, other):
    return self.salary + other.salary


def __sub__(self, other):
    return self.salary - other.salary


def __str__(self):
    return f"MedicalStaff({self.name}, {self.age}, {self.salary})"


def __repr__(self):
    return f"MedicalStaff({self.name}, {self.age}, {self.salary})"
