from django.db import models

# Create your models here.
CASETYPE = (
    ('', 'Please Select Case Category'),
    ('Tax Matters', 'Tax Matters'),
    ('Employment', 'Employment'),
    ('Business Transaction', 'Business Transaction'),
    ('Debt Recovery', 'Debt Recovery'),
    ('Civil Matters', 'Civil Matters'),
    ('Child Custody', 'Child Custody'),
    ('Divorce', 'Divorce'),
    ('Property', 'Property'),
    ('Dispute', 'Dispute'),
    ('Immigration', 'Immigration')
)

GENDER = (
    ('', 'Select Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unknown', 'Unknown'),
)

LAWYERTYPE = (
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

SITUATION = (
    ('', 'Case Status'),
    ('Completed', 'Completed'),
    ('InProgress', 'InProgress'),
    ('Dismissed', 'Dismissed')
)

SKILLS = (
    ('', 'Select a Skill'),
    ('Analytical and research skills', 'Completed'),
    ('Attention to detail', 'Attention to detail'),
    ('Organizational Skills', 'Organizational Skills'),
    ('Time Management', 'Time Management'),
    ('Persuasive communication', 'Persuasive communication')
)


class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10, null=True, choices=GENDER)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    case_type = models.CharField(max_length=100, null=True, choices=CASETYPE)
    description = models.TextField()
    profile = models.ImageField(blank=True, upload_to='pics', default='profile_picture')
    reg_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)


class Lawyer(models.Model):
    Firm = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=100)
    Lawyer_type = models.CharField(
        max_length=100, null=True, choices=LAWYERTYPE)
    Experience = models.CharField(max_length=50)
    skills = models.CharField(max_length=100, choices=SKILLS)
    Gender = models.CharField(max_length=100, null=True, choices=GENDER)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=100)
    Zip = models.CharField(max_length=6)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=16)
    Phone = models.CharField(max_length=15)
    Profile = models.ImageField(blank=True, upload_to='pics', default='profile_picture')
    reg_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.FirstName)


class Cases(models.Model):
    case_id = models.CharField(max_length=10)
    case_type = models.CharField(max_length=50, choices=CASETYPE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    situation = models.CharField(
        max_length=50, null=True, choices=SITUATION, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.case_id

    class Meta:
        verbose_name = 'cases'
        verbose_name_plural = 'cases'
