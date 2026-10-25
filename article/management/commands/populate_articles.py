from django.core.management.base import BaseCommand
from article.models import Article

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating articles...")

        for i in range(1, 56):
            if i % 5 == 0:
                is_pub = False
            else:
                is_pub = True
            
            Article.objects.create(
                title=f"Article Title {i}",
                content=f"This is the content for article {i}. It has some information.",
                author=f"Author {((i - 1) % 5) + 1}",
                is_published=is_pub
            )

        self.stdout.write(self.style.SUCCESS("Successfully created articles!"))
