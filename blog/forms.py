from django import forms
from blog.models import Comment

class CommentForm(forms.Form):
    user = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)

class CommentOriginalForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)