from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import *
from .forms import ArticleForm, AuthorForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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

@login_required
def article_form(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Article.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("homepage"))


    form = ArticleForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def author_form(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
                Author.objects.create(
                    name = data.get('name'),
                    user = new_user,
                    bio = data.get('bio')
                )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        return HttpResponse("This action is forbidden")
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user) #sets session cookie, server has recognized this user as being authorized, magic piece
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))) #need to figure out the re-dir later but thankfully we're on the back end and WE dont CARE! JKJK figure out how to direct this after the request has been made 

    form = LoginForm() #fallback if we get the wrong info
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))