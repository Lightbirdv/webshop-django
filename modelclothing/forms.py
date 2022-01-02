from django import forms
from .models import Clothing, Comment


class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name', 'description', 'color', 'collection', 'size', 'type']
        widgets = {
            'size': forms.Select(choices=Clothing.SIZE),
            'type': forms.Select(choices=Clothing.TYPE),
            'myuser': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'myuser': forms.HiddenInput(),
            'clothing': forms.HiddenInput(),
        }

        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name']