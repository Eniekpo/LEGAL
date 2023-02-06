from django.db import models
# Create your models here.
REQUEST = (
    ('', 'Please Select Case Category'),
    ('Tax Matters', 'Tax Matters'),
    ('Employment', 'Employment'),
    ('Business Transaction', 'Business Transaction'),
    ('Debt Recovery', 'Debt Recovery'),
    ('Civil Matters', 'Civil Matters'),
    ('Child Custody', 'Child Custody'),
    ('Property', 'Property'),
    ('Disput', 'Disput'),
    ('Immigration', 'Immigration')
)

GENDER = (
    ('', 'Gender'),
    ('Male', 'Male'),
    ('Female', 'Female')
)

CATEGORY = (
    ('', 'Select Lawyer Category'),
    ('Tax Lawyer', 'Tax Lawyer'),
    ('Immigration Lawyer', 'Immigration Lawyer'),
    ('Transactional Lawyer', 'Transactional Lawyer'),
    ('Public Interest Lawyer', 'Public Interest Lawyer'),
    ('Dispute Resolution Lawyer', 'Dispute Resolution Lawyer'),
    ('Worker Compensation Lawyer', 'Worker Compensation Lawyer'),
    ('Contract Lawyer', 'Contract Lawyer'),
    ('Civil Litigation Lawyer', 'Civil Litigation Lawyer'),
    ('Social Security Disability Lawyer', 'Social Security Disability Lawyer'),
    ('General Practice Lawyer', 'General Practice Lawyer')
)


class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=10, null=True, choices=GENDER)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    request = models.CharField(max_length=100, null=True, choices=REQUEST)
    description = models.TextField()
    reg_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)


class Lawyer(models.Model):
    Company = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    Experience = models.CharField(max_length=50)
    Gender = models.CharField(max_length=100, null=True, choices=GENDER)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    reg_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.FirstName)
