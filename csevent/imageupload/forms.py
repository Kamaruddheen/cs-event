from django.forms import ModelForm
from .models import *


class LogoForm(ModelForm):

    class Meta:
        model = Logo
        fields = ['logo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo'].label = "Upload your Logo"


class PosterForm(ModelForm):

    class Meta:
        model = Poster
        fields = ['poster']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['poster'].label = "Upload your Poster"
