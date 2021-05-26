from admin1.models import *
from django import forms
from django.core import validators


class storecsvdataForm(forms.ModelForm):

    class Meta():
        model = csvdatamodel
        fields = '__all__'


