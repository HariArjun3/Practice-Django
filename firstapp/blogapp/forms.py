from django.forms import ModelForm
from .models import Blog
from django import forms


class BlogPostForm(forms.Form):
    Blog_title = forms.CharField(max_length=100,  required=False)
    Author_name = forms.CharField(max_length=100,  required=False)
    Blog_content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 60}),  required=False)





    # class Meta:
    #     model = BlogPost
    #     fields = ['title', 'author', 'content']
