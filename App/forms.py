from django import forms
from . models import Client, Lawyer, Cases
from django.core.validators import RegexValidator


class ClientForm(forms.ModelForm):

    # VALIDATIONS
    firstname = forms.CharField(
        label='First Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    lastname = forms.CharField(
        label='Last Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    email = forms.CharField(
        label='Email Address', min_length=10, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$',
                                   message='Put a valid email address !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'})
    )

    city = forms.CharField(
        label='City', min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only Letters is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Lagos'})
    )

    state = forms.CharField(
        label='State', min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only Letters is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bayelsa'})
    )

    description = forms.CharField(
        label='Additional Details', min_length=20, max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Briefly describe your case', 'rows': 5}
        )
    )

    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'phone': forms.TextInput(
                attrs={'style': 'font-size:18px',
                       'placeholder': 'Phone Number',
                       'data-mask': '(000) 000000 0000'
                       }
            )
        }
       
           
        


class LawyerForm(forms.ModelForm):

    Firm = forms.CharField(
        label='Company Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Company Name'})
    )

    FirstName = forms.CharField(
        label='First Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    LastName = forms.CharField(
        label='Last Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    Experience = forms.CharField(
        label='Experience', min_length=3, max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Experience'})
    )

    Email = forms.CharField(
        label='Email Address', min_length=10, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$',
                                   message='Put a valid email address !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'})
    )
    City = forms.CharField(
        label='City', min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only Letters is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Lagos'})
    )

    State = forms.CharField(
        label='State', min_length=3, max_length=30,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only Letters is allowed !')],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bayelsa'})
    )

    class Meta:
        model = Lawyer
        fields = "__all__"
        widgets = {
            'Password': forms.PasswordInput(),
            'Phone': forms.TextInput(
                attrs={'style': 'font-size:18px',
                       'placeholder': 'Phone Number',
                       'data-mask': '(000) 000000 0000'
                       }
            )
        }


class CasesForm(forms.Form):
    class Meta:
        model = Cases
        exclude = ("created_at", "situation")

        #  'SUPER' FUNCTION

    def __init__(self, *args, **kwargs):
        super(CasesForm, self).__init__(*args, **kwargs)
