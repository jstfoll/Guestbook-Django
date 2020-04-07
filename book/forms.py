from django import forms

class commentform(forms.Form):
    name=forms.CharField(max_length='20' , widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    comment=forms.CharField(max_length='100',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))