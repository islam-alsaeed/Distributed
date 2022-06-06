import imp
from tkinter import Widget
from django import forms
from .models import Book,Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'pages',
            'price',
            'retail_price_day',
            'retail_period',
            'status',
            'category',
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'book_photo': forms.FileInput(attrs={'class':'form-control'}),
            'author_photo': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retail_price_day': forms.NumberInput(attrs={'class':'form-control'},),
            'retail_period': forms.NumberInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }