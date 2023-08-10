from django import forms

from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.TextInput)



class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
