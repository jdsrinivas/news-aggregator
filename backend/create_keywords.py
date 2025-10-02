import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsaggregator.settings')
django.setup()

from news.models import Keyword

# 10 default keywords for news sections
keywords_data = [
    (1, "Technology"),
    (2, "Business"),
    (3, "Politics"),
    (4, "Health"),
    (5, "Science"),
    (6, "Sports"),
    (7, "Entertainment"),
    (8, "Environment"),
    (9, "Education"),
    (10, "Travel"),
]

for section_number, name in keywords_data:
    keyword, created = Keyword.objects.get_or_create(
        section_number=section_number,
        defaults={'name': name}
    )
    if created:
        print(f"Created keyword: {section_number}. {name}")
    else:
        print(f"Keyword already exists: {section_number}. {name}")

print("\nKeywords setup complete!")
