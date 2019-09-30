from django import forms
from firstapp.models import MySiteUser

class MySiteUserForm(forms.ModelForm):
    class Meta():
        model=MySiteUser
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive"
                ]