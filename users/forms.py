# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
#from apps.breaks.models import Break
from django.contrib.auth.models import User
import re

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        # username in password position
        value = self.fields.pop('username')
        new_pos = self.fields.keyOrder.index('password')
        self.fields.insert(new_pos, 'username', value)

        # is_superuser
        value = self.fields.pop('is_superuser')
        new_pos = self.fields.keyOrder.index('is_staff')
        self.fields.insert(new_pos, 'is_superuser', value)

        self.fields['is_superuser'].label = u"Is superuser?"
        self.fields['is_superuser'].help_text = u""
        self.fields['is_staff'].label = u"Is staff?"
        self.fields['is_staff'].help_text = u""

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        exclude = ('last_login','date_joined','user_permissions','groups')

class LoginForm(forms.Form):
    login = forms.CharField(label=u"Username", max_length=30)
    password = forms.CharField(label=u"Password",max_length=100,widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class PasswordForm(forms.Form):
    password = forms.CharField(label=u"Current password",max_length=100,widget=forms.PasswordInput())
    new_password = forms.CharField(label=u"New password",max_length=100,widget=forms.PasswordInput())
    confirm_password = forms.CharField(label=u"Confirm password",max_length=100,widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
