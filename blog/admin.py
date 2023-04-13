from django.contrib import admin
from .models import Article, Category, Comment, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'image', 'content', 'created_date']
    list_filter = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ['tags', ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'author', 'article', 'created_date']
#     date_hierarchy = 'created_date'


admin.site.register(Comment)