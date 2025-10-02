from apscheduler.schedulers.background import BackgroundScheduler
from .news_fetcher import NewsFetcher


def start_scheduler():
    """Start the background scheduler for hourly news updates"""
    scheduler = BackgroundScheduler()
    fetcher = NewsFetcher()
    
    # Schedule the job to run every hour
    scheduler.add_job(
        fetcher.fetch_all_news,
        'interval',
        hours=1,
        id='fetch_news_hourly',
        replace_existing=True
    )
    
    scheduler.start()
    print("News scheduler started - will fetch news every hour")
    
    return scheduler
