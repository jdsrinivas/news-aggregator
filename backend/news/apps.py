from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    
    def ready(self):
        # Start the scheduler when Django starts
        from .scheduler import start_scheduler
        import os
        
        # Only start scheduler in the main process (not in the reloader process)
        if os.environ.get('RUN_MAIN', None) == 'true':
            start_scheduler()
