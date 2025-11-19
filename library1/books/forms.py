from django import forms

# class Addbooksform(forms. Form):
#     # title=forms.CharField()
#     # author=forms.CharField()
#     # price=forms.IntegerField()
#     # pages=forms.IntegerField()
#     # language = forms.CharField()
#
from books.models import Book

class Addbooksform(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"




