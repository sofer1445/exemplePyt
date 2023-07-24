class MedicalStaff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Nurse(MedicalStaff):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def __str__(self):
        return super.to_string(self)

    def __repr__(self):
        return f"Nurse({self.name}, {self.age}, {self.salary}, {self.department})"


