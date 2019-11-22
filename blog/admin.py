from django.contrib import admin
from . import models
from django.utils import timezone


@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'Post',
        'Name',
        'Email',
        'Text',
        'Approved',
        'created',
        'updated',

    )

    list_filter = (
        'Approved',
        )
    search_fields = (
        'Name',
        'Email',
        'Text',
        )

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
      'name',
      'slug',
    )

    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = (
    'title',
    'author',
    'created',
    'updated'
    )

    list_filter = (
     'status',
     'topics',
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
