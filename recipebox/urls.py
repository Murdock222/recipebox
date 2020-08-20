"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox_app.views import index, about_author, about_recipe, article_form, author_form, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="homepage"),
    path('recipe/<int:recipe_id>/', about_recipe),
    path('author/<int:author_id>/', about_author),
    path('newarticle/', article_form, name="newarticle"),
    # path('articleform/', article_form, name="newarticle"),
    path('newauthor/', author_form, name="newauthor"),
    path('login/', login_view, name="loginview"),
    path('logout/', logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
] 
