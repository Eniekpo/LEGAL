from django import forms
from . models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["firstname", "lastname", "email", "gender", "city",
                  "state", "phone", "description"]
