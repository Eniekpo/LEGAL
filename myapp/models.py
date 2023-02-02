from django.db import models
# Create your models here.


class Case(models.Model):
    Case_Category = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Case_Category)


class Lawyercat(models.Model):
    Lawyer_Category = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Lawyer_Category)


class Lawyer(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=100)
    Category = models.ForeignKey(
        Lawyercat, on_delete=models.CASCADE)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return str(self.FirstName)


class Client(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=100)
    Case_Category = models.ForeignKey(
        Case, on_delete=models.CASCADE)
    Lawyer = models.ForeignKey(
        Lawyer, on_delete=models.CASCADE)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return str(self.FirstName)
