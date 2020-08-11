from django import forms
from recipebox_app.models import Article, Author

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]