from django import forms
from .models import Author

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]