from django.contrib import admin

# Register your models here.
from recipebox_app.models import Article, Author

admin.site.register(Article)
admin.site.register(Author)
