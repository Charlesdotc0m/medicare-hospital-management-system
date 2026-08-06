from django.db import models


# Department Model
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_description = models.TextField()

    def __str__(self):
        return self.department_name


# Doctor Model
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_specialization = models.CharField(max_length=100)
    doctor_image = models.ImageField(upload_to='doctors/')
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name


# Patient Model
class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_phone = models.CharField(max_length=15)
    patient_email = models.EmailField()
    patient_problem = models.TextField()

    def __str__(self):
        return self.patient_name



# Appointment Model
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return self.patient_name
