from django import forms

from .models import *


class UserForm(forms.ModelForm):
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter your Mobile Number'}), label="Mobile Number :")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', }), label="Password :")
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}), label="Confirm Password :")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile',
                  'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'Enter your First name', 'class': 'input_cust capitalize'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Enter your Last name', 'class': 'input_cust capitalize'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'eg..abc@example.com', 'class': 'input_cust'})

        self.fields['email'].label = "Email Address :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['first_name'].label = "First Name :"

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
        fields = ['college', 'dept',
                  'roll_no', 'id_proof', 'profile_pic', 'bonafide', 'college_address', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['college_address'].widget.attrs.update(
            {'placeholder': 'Full address of your college', 'rows': '5'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Enter your residential address', 'rows': '5'})

        self.fields['college'].label = "Name of the College :"
        self.fields['dept'].label = "Department :"
        self.fields['roll_no'].label = "Roll Number :"
        self.fields['id_proof'].label = "Identity Card :"
        self.fields['profile_pic'].label = "Participant Photo :"
        self.fields['college_address'].label = "College Address :"
        self.fields['address'].label = "Address :"
        self.fields['bonafide'].label = "Bonafide :"
        self.fields['bonafide'].required = False


# Myaccount
class User_Form(forms.ModelForm):
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter your Mobile Number'}), label="Mobile Number :")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'Enter your First name'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Enter your Last name'})

        self.fields['last_name'].label = "Last Name :"
        self.fields['first_name'].label = "First Name :"

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
