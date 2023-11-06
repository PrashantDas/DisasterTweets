from django import forms

class MyForm(forms.Form):
    STYLE = {'cols':30, 'rows':6, 'placeholder':'Forest Fire'}
    text = forms.CharField(widget=forms.Textarea(attrs=STYLE))
