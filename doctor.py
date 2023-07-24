class MedicalStaff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Doctor(MedicalStaff):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, salary)
        self.specialization = specialization

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"Doctor({self.name}, {self.age}, {self.salary}, {self.specialty})"
