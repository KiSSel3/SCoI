from django import forms
from .models import Device,Issue
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'image']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер кабинета',
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка кабинета'
            }),

        }

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'price', 'device_type']

        widgets = {
            "issue_type": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка кабинета',
            }),
            "price": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка кабинета',
            }),
            "device_type": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка кабинета',
            }),

        }