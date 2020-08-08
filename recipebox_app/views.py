from django.shortcuts import render
from .models import *

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