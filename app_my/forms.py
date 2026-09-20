from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Category, Tag, Quote

User = get_user_model()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'created_by']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'category', 'created_by', 'tags']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']