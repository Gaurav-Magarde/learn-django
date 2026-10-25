# Note: Django looks for management commands in `article/management/commands/populate_articles.py`.
# This file is kept here as well for your reference.
from django.core.management.base import BaseCommand
from article.models import Article

class Command(BaseCommand):
    help = 'Populates the database with sample articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating articles...")

        for i in range(1, 56):
            is_pub = False if i % 5 == 0 else True
            
            Article.objects.create(
                title=f"Sample Article Title {i}",
                content=f"This is the sample content for article number {i}. It has some interesting information.",
                author=f"Author {((i - 1) % 5) + 1}",
                is_published=is_pub
            )

        self.stdout.write(self.style.SUCCESS("Successfully created 55 articles!"))
