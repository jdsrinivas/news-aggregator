from rest_framework import serializers
from .models import Keyword, NewsArticle


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'description', 'url', 'source', 'published_at', 'image_url', 'fetched_at']


class KeywordSerializer(serializers.ModelSerializer):
    articles = NewsArticleSerializer(many=True, read_only=True)
    article_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Keyword
        fields = ['id', 'name', 'section_number', 'created_at', 'articles', 'article_count']
    
    def get_article_count(self, obj):
        return obj.articles.count()
