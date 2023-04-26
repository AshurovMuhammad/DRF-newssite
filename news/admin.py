from django.contrib import admin
from .models import News, Category

admin.site.registrer(News)
admin.site.registrer(Category)
