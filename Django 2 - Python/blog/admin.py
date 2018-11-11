from django.contrib import admin
from django.db import models
from django.forms import Textarea

from blog.models import PostCategory, Post, Comment


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'published',
        'created_at',
        'comments_count',
    )

    list_filter = (
        'category__name',
        'published',
    )

    autocomplete_fields = ['category']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})},
    }

    def comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()
    comments_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ['post__title', 'author_name', ]
    list_display = (
        'post',
        'author_name',
        'status',
        'moderation_text',
        'created_at',
        'text',
    )

    list_editable = ('status', 'moderation_text', )

    list_filter = ('status', )
