# forms.py
from django import forms

class MyForm(forms.Form):
    ausente = forms.BooleanField(required=False)
    enable_input = forms.BooleanField(required=False)
    text_input = forms.CharField(required=False, widget=forms.TextInput(attrs={'disabled': 'disabled'}))
