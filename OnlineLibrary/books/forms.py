from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='message', max_length=2000)
