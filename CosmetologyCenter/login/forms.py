from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=200,
                                 help_text='Enter first name')
    last_name = forms.CharField(max_length=200,
                                help_text='Enter last name')
    date_of_birth = forms.DateField()
    phone_number = forms.CharField(max_length=50,
                                   help_text='Enter phone number',
                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX',
                                   )])

    class Meta:
        model = CustomUser
        fields = {'username', 'email', 'first_name',
                  'last_name', 'date_of_birth',
                  'phone_number', 'password1',
                  'password2'
                  }