from django import forms
from .models import Art


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        exclude = ["user", "image"]

