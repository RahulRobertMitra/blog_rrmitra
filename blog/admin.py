from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
    'title',
    'author',
    'created',
    'updated'
    )
    search_fields = (
    'title',
    'author__username',
    'author__first_name',
    'author__last_name',
    )
    prepopulated_fields = {
      'slug': ('title',)
    }
    pass

admin.site.register(models.Post, PostAdmin)