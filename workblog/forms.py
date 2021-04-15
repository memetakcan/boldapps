from django import forms
from .models import *

class WorkchartForm(forms.ModelForm):

    class Meta:
        model = Workchart
        fields=["project","projectpart","content"]