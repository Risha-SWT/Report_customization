# carbone_app/forms.py
from django import forms
from .models import CarboneRender

class CarboneRenderForm(forms.ModelForm):
    class Meta:
        model = CarboneRender
        fields = ['template_file', 'json_file']