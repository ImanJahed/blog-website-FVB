from tkinter import Widget
from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username: ')
    password = forms.CharField(label='Password: ', widget=forms.PasswordInput)



class UserEditForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="alert alert-danger">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])


class UserEdit(forms.ModelForm):
    # error_css_class = 'alert alert-danger'
    # def __init__(self, error_class,*args, **kwargs ):
    #     super().__init__(error_class,*args, **kwargs)
    #     error_class = 'alert alert-danger'
    class Meta:
        # error_class = "alert alert-danger"
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':"form-control"}),
            'last_name': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
        
            
        }
        errors = {
            "email": {"attrs":{'errorlist': "alert alert-danger"}}
        }
        # fields_error_classes = {
        #     "email": {"attrs":{'class': "alert alert-danger"}}
        # }