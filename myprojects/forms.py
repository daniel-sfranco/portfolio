from django import forms
from . import models

class CreateProject(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'body', 'git', 'banner']
