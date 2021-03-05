from django import forms

from .models import *


class Student_Answer(forms.ModelForm):

    class Meta:
        model = Stud_Res_WordHunt
        fields = ['user_answer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_answer'].widget.attrs.update(
            {'placeholder': 'Enter your answer'})
        self.fields['user_answer'].label = "Answer :"
