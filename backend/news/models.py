from django.db import models
from django.utils import timezone


class Keyword(models.Model):
    name = models.CharField(max_length=200, unique=True)
    section_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['section_number']

    def __str__(self):
        return f"{self.section_number}. {self.name}"


class NewsArticle(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=1000)
    source = models.CharField(max_length=200, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    fetched_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']
        unique_together = ['keyword', 'url']

    def __str__(self):
        return self.title
