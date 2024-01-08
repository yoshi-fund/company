from django import forms
from .models import Company

class Company_forms(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

        