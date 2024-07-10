from django import forms
from .models import post

class = PostForm(forms.ModelForm):
    class = Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'created_on',)

        wigets = {
            'title': form.TextInput(attrs={'class':'form-control'}),
            'author': form.Select(attrs={'class':'form-control'}),
            'content': form.Textarea(attrs={'class':'form-control'}),
            'slug': form.TextInput(attrs={'class':'form-control'}),

        }