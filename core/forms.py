# email form 


from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ReviewForm(forms.Form):
    stars = forms.IntegerField(max_value=5, min_value=0)
    comment = forms.CharField(widget=forms.Textarea)