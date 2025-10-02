from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Keyword, NewsArticle
from .serializers import KeywordSerializer, NewsArticleSerializer
from .news_fetcher import NewsFetcher


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    
    @action(detail=False, methods=['post'])
    def refresh_news(self, request):
        """Manually trigger news refresh for all keywords"""
        fetcher = NewsFetcher()
        total_articles = fetcher.fetch_all_news()
        return Response({
            'message': f'Successfully fetched {total_articles} articles',
            'total_articles': total_articles
        })
    
    @action(detail=True, methods=['post'])
    def refresh_keyword(self, request, pk=None):
        """Refresh news for a specific keyword"""
        keyword = self.get_object()
        fetcher = NewsFetcher()
        count = fetcher.fetch_news_for_keyword(keyword)
        return Response({
            'message': f'Fetched {count} articles for {keyword.name}',
            'article_count': count
        })


class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    
    def get_queryset(self):
        queryset = NewsArticle.objects.all()
        keyword_id = self.request.query_params.get('keyword', None)
        if keyword_id is not None:
            queryset = queryset.filter(keyword_id=keyword_id)
        return queryset
