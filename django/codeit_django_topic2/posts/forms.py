from dataclasses import field
from django import forms
from posts.models import Post

# 방법 1
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=50, label="제목")
#     content = forms.CharField(label="내용", widget=forms.Textarea)

# 방법 2
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # fields = ['title', 'content']
        fields = '__all__'