from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image1', 'image2', 'image3']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the post title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the post content'})
        self.fields['image1'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['image2'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['image3'].widget.attrs.update({'class': 'form-control-file'})


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'image1', 'image2', 'image3']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Edit the post title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Edit the post content'})
        self.fields['tag'].widget.attrs.update({'class': 'form-control'})

        self.fields['image1'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['image2'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['image3'].widget.attrs.update({'class': 'form-control-file'})