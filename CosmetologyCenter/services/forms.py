from django import forms
from .models import Device,Issue
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'image']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'картинка устройства'
            }),

        }

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'price', 'device_type']

        widgets = {
            "issue_type": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "price": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),
            "device_type": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'название устройства',
            }),

        }