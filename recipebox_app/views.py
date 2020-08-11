from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from .forms import ArticleForm, AuthorForm

# Create your views here.
def index(request):
    my_recipes = Article.objects.all()
    return render(request, "index.html", {"key": "HELLO RECIPE", "recipes": my_recipes})

def about_author(request, author_id):
    this_author = Author.objects.filter(id=author_id).first()
    recipe_article = Article.objects.filter(author=this_author)
    return render(request, "author_info.html", {"author": this_author, "recipes": recipe_article})

def about_recipe(request, recipe_id):
    this_recipe = Article.objects.filter(id=recipe_id).first()
    return render(request, "recipe_info.html", {"recipe": this_recipe})

def article_form(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Article.objects.create(
                title=data.get('title'),
                # body=data.get('body'),
                # description=data.get('description'),
                author=data.get('author')
            )
            return HttpResponseRedirect(reverse("homepage"))


    form = ArticleForm()
    return render(request, "generic_form.html", {"form": form})

def author_form(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})