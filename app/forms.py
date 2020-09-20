from django import forms
from app.models import BashScript

class SearchBox(forms.Form):
    search =  forms.CharField(max_length=100, label='Search Box')
