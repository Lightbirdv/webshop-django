from django import forms
from .models import Clothing, Comment


class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ['name', 'description', 'color', 'collection', 'size', 'type', 'sex','pdffile', 'product_picture', 'price']
        widgets = {
            'size': forms.Select(choices=Clothing.SIZE, attrs={'class': 'choice__input'}),
            'type': forms.Select(choices=Clothing.TYPE, attrs={'class': 'choice__input'}),
            'sex': forms.Select(choices=Clothing.SEX, attrs={'class': 'choice__input'}),
            'myuser': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'txt__input'}),
            'description': forms.TextInput(attrs={'class': 'txt__input'}),
            'color': forms.TextInput(attrs={'class': 'txt__input'}),
            'collection': forms.TextInput(attrs={'class': 'txt__input'}),
            'price': forms.TextInput(attrs={'class': 'txt__input'}),
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