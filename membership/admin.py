from django.contrib import admin
from .models import Article


class Articleadmin(admin.ModelAdmin):

    list_display = (
        'date_published',
        'headline',
        'article',
        'author',
        'image',
    )


admin.site.register(Article, Articleadmin)
