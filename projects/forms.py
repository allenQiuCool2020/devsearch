from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.forms.utils import ErrorList
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add Title'})

        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Add Description'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        label = {
            'value':'Place your vote',
            'body': 'Add a comment with your vote'
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
