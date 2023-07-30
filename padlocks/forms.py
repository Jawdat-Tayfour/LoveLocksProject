from django import forms 
from django.forms import ModelForm


from .models import PadLock

class PadLockForm(ModelForm):
    class Meta:
        model = PadLock
        fields = ('start_date','motto_field','story_field')