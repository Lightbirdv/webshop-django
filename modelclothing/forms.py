from django import forms
from .models import Clothing, Comment


class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name', 'description', 'color', 'collection', 'size', 'type']
        widgets = {
            'size': forms.Select(choices=Clothing.SIZE),
            'type': forms.Select(choices=Clothing.TYPE),
            'user': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'clothing': forms.HiddenInput(),
        }