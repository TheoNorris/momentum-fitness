from django.contrib import admin
from .models import MembersPage


class MembersPageadmin(admin.ModelAdmin):

    list_display = (
        'date_published',
        'headline',
        'article',
        'author',
        'image',
    )


admin.site.register(MembersPage, MembersPageadmin)
