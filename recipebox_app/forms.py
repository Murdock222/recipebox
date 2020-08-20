from django import forms
from .models import Author, Article

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)

class AuthorForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=200)
    bio = forms.CharField(widget=forms.Textarea)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

# class LogoutForm(forms.Form):
