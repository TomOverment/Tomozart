from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class  Meta:
        model = Post
        fields = ('title', 'author', 'content',)

        wigets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Post Title'}),
            'author': forms.Select(attrs={'class':'form-control', 'placeholder' : 'Username'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Comment here'}),
            #'slug': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class  Meta:
        model = Post
        fields = ('title','author', 'content',)

        wigets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Post Title'}),
            #'author': forms.Select(attrs={'class':'form-control', 'placeholder' : 'Username'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Comment here'}),
            #'slug': forms.TextInput(attrs={'class':'form-control'}),

        }