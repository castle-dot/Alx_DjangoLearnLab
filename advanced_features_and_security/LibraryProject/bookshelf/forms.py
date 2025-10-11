# forms.py

from django import forms

class ExampleForm(forms.Form):
    example_input = forms.CharField(max_length=100)
