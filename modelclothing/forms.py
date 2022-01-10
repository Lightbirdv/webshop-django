from django import forms
from .models import Clothing, Comment


class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name', 'description', 'color', 'collection', 'size', 'type', 'sex','pdffile', 'product_picture', 'price']
        widgets = {
            'size': forms.Select(choices=Clothing.SIZE),
            'type': forms.Select(choices=Clothing.TYPE),
            'sex': forms.Select(choices=Clothing.SEX),
            'myuser': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'myuser': forms.HiddenInput(),
            'clothing': forms.HiddenInput(),
        }

        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name','description']