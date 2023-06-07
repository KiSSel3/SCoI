from django import forms

Issue_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartIssueAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=Issue_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)