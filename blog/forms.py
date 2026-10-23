from django import forms

class contactform(forms.Form):
    name=forms.CharField(max_length=100,label='Name',required=True)
    email=forms.EmailField(label='Email',max_length=100,required=True)
    message=forms.CharField(widget=forms.Textarea,label='Message',max_length=500,required=True)