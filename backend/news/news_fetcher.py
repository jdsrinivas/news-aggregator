import requests
from datetime import datetime
from .models import Keyword, NewsArticle

class NewsFetcher:
    def __init__(self):
        # Using NewsAPI.org - Free tier allows 100 requests/day
        # For production, users should get their own API key from https://newsapi.org
        self.api_key = 'demo'  # Replace with actual API key
        self.base_url = 'https://newsapi.org/v2/everything'
    
    def fetch_news_for_keyword(self, keyword):
        """Fetch news articles for a specific keyword"""
        try:
            params = {
                'q': keyword.name,
                'apiKey': self.api_key,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 10
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                articles_saved = 0
                
                for article_data in data.get('articles', []):
                    # Skip articles without required fields
                    if not article_data.get('url') or not article_data.get('title'):
                        continue
                    
                    # Parse published date
                    published_at = None
                    if article_data.get('publishedAt'):
                        try:
                            published_at = datetime.fromisoformat(
                                article_data['publishedAt'].replace('Z', '+00:00')
                            )
                        except:
                            pass
                    
                    # Create or update article
                    NewsArticle.objects.get_or_create(
                        keyword=keyword,
                        url=article_data['url'],
                        defaults={
                            'title': article_data.get('title', '')[:500],
                            'description': article_data.get('description', ''),
                            'source': article_data.get('source', {}).get('name', ''),
                            'published_at': published_at,
                            'image_url': article_data.get('urlToImage', ''),
                        }
                    )
                    articles_saved += 1
                
                return articles_saved
            else:
                print(f"Error fetching news for {keyword.name}: {response.status_code}")
                return 0
                
        except Exception as e:
            print(f"Exception fetching news for {keyword.name}: {str(e)}")
            return 0
    
    def fetch_all_news(self):
        """Fetch news for all keywords"""
        keywords = Keyword.objects.all()
        total_articles = 0
        
        for keyword in keywords:
            count = self.fetch_news_for_keyword(keyword)
            total_articles += count
            print(f"Fetched {count} articles for {keyword.name}")
        
        return total_articles
