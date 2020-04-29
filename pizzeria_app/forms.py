from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text','comment_author']
        labels = {'comment_text':'', 'comment_author':'Your Name'}