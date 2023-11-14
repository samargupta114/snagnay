from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib import messages
import re

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean(self):
        super(TeacherUserForm, self).clean();
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        SpecialSym =['$', '@', '#', '%']
        val = True
          
        if len(password) < 6:
            print('length should be at least 6')
            val = False
              
        if len(password) > 20:
            print('length should be not be greater than 8')
            val = False
              
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False
              
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False
              
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False
              
        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            val = False
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if val==False:
            self._errors['password'] = self.error_class([
                'password should contain minimum of 8 characters'])
        return self.cleaned_data


class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields=['address','mobile','profile_pic']
    def clean(self):
        super(TeacherForm, self).clean();
        mobile = self.cleaned_data.get('mobile')
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        
        if Pattern.match(mobile)==False:
            self._errors['mobile'] = self.error_class([
                'Minimum 10 characters required'])

