from django.contrib import admin
from .models import Article
from .models import Author

admin.site.register(Article)
admin.site.register(Author)
# Register your models here.
