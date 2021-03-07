from django import forms

from .models import *


class UserForm(forms.ModelForm):
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Mobile Number...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', }), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}), label="Confirm Password")

    class Meta:
        model = User
        fields = fields = ['first_name', 'last_name', 'mobile',
                           'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email

    def clean_confirm_password(self):
        c_pass = self.cleaned_data.get('confirm_password')
        if not c_pass == self.cleaned_data.get('password'):
            raise forms.ValidationError('Password did not match')
        return c_pass

    # validating the mobile no
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not len(mobile) == 10:
            raise forms.ValidationError('Enter a valid Mobile Number')
        if not mobile.isnumeric():
            raise forms.ValidationError('Mobile Number must be a Integer')
        return mobile


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = fields = ['college', 'dept',
                           'roll_no', 'id_proof', 'profile_pic', 'bonafide']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['college'].label = "Name of the College : "
        self.fields['dept'].label = "Department : "
        self.fields['roll_no'].label = "Roll Number : "
        self.fields['id_proof'].label = "Identity Card : "
        self.fields['profile_pic'].label = "Personal Image : "
        self.fields['bonafide'].label = "Bonafide : "
        self.fields['bonafide'].required = False
