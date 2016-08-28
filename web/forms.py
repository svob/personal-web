from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=200, required=False,
                             widget=forms.EmailInput(attrs={'placeholder': 'E-Mail'}))
    phone = forms.CharField(max_length=50, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=False)