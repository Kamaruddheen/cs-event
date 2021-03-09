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


class LogoFinalForm(ModelForm):

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


class LogoScoreForm(ModelForm):
    class Meta:
        model = Logo
        fields = ['score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].widget.attrs.update(
            {'placeholder': 'Score..'})


class PosterScoreForm(ModelForm):
    class Meta:
        model = Poster
        fields = ['score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].widget.attrs.update(
            {'placeholder': 'Score..'})
