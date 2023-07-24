# operating the hospital
from patient import Patient
from hospital import Hospital
from medical_staff import Medical_Staff
from doctor import Doctor
from nurse import Nurse


def main():
    # Create a hospital
    hospital = Hospital("Hospital", 5)

    # Create a doctor
    doctor = Doctor("John", 30, 100000, "Pediatrician")

    # Create a nurse
    nurse = Nurse("Jane", 25, 50000, "Pediatric Nurse")

    # Create a patient
    patient = Patient(1, "Alex", "None")

    # Admit a patient
    hospital.admit(patient)

    # Assign a doctor and a nurse to the patient
    patient.assign_doctor(doctor)
    patient.assign_nurse(nurse)

    # Display patient information
    patient.display_info()

    # Discharge the patient
    patient.discharge(hospital)


if __name__ == "__main__":
    main()
