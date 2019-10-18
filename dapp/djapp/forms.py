from django import forms

class kakikomiForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField()
    