from django.db import models

# Create your models here.
class Patient(models.Model):
    """Patient's personal information"""
    Name = models.CharField(max_length = 100)
    Gender = models.CharField(max_length = 20)
    YearofBirth = models.DateField()
    Location = models.CharField(max_length = 50)
    PreviousAppointment = models.DateField()
    NextAppointment = models.DateField()
    BloodPressure1 = models.IntegerField()
    BloodPressure2 = models.IntegerField()
    BloodPressure3 = models.IntegerField()
    BloodPressure4 = models.IntegerField()
    BloodPressure5 = models.IntegerField()

    def __str__(self):
        return self.name