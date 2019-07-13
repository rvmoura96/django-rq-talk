from django import forms

from .models import FibNumber


class FibNumberForm(forms.ModelForm):
    class Meta:
        model = FibNumber
        fields = ["original_number"]
