from django.forms import ModelForm
from .models import *


class LogoForm(ModelForm):

    class Meta:
        model = Logo
        fields = ['logo', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Describe your logo', 'rows': '5'})
        self.fields['logo'].label = "Upload your Logo"
        self.fields['description'].label = "Description : "
        self.fields['description'].required = False


class PosterForm(ModelForm):

    class Meta:
        model = Poster
        fields = ['poster']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['poster'].label = "Upload your Poster"
