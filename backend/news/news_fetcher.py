import requests
from datetime import datetime
from .models import Keyword, NewsArticle
import feedparser
import re

class NewsFetcher:
    def __init__(self):
        # Using RSS feeds from Google News (no API key required)
        # For better results, get a free API key from https://newsapi.org
        self.use_rss = True
    
    def fetch_news_for_keyword(self, keyword):
        """Fetch news articles for a specific keyword"""
        try:
            # Use Google News RSS feed (no API key required)
            rss_url = f'https://news.google.com/rss/search?q={keyword.name}&hl=en-US&gl=US&ceid=US:en'
            
            feed = feedparser.parse(rss_url)
            articles_saved = 0
            
            for entry in feed.entries[:10]:  # Limit to 10 articles
                # Skip articles without required fields
                if not entry.get('link') or not entry.get('title'):
                    continue
                
                # Parse published date
                published_at = None
                if entry.get('published_parsed'):
                    try:
                        published_at = datetime(*entry.published_parsed[:6])
                    except:
                        pass
                
                # Extract description
                description = entry.get('summary', entry.get('description', ''))
                if description:
                    # Clean HTML tags from description
                    description = re.sub('<[^<]+?>', '', description)
                
                # Create or update article
                NewsArticle.objects.get_or_create(
                    keyword=keyword,
                    url=entry.link,
                    defaults={
                        'title': entry.title[:500],
                        'description': description[:1000] if description else '',
                        'source': entry.get('source', {}).get('title', 'Google News'),
                        'published_at': published_at,
                        'image_url': '',
                    }
                )
                articles_saved += 1
            
            return articles_saved
                
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
