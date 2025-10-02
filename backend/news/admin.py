from django.contrib import admin
from .models import Keyword, NewsArticle


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['section_number', 'name', 'created_at']
    list_filter = ['section_number']
    search_fields = ['name']
    ordering = ['section_number']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'keyword', 'source', 'published_at', 'fetched_at']
    list_filter = ['keyword', 'source', 'published_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'published_at'
