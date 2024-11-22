from django import forms
from .models import Books, Lectures

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'file']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class LectureUploadForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ['title', 'description', 'file', 'subject']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lecture Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Lecture Description'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }