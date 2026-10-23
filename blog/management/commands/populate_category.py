
from django.core.management.base import BaseCommand
from blog.models import Post, category


class Command(BaseCommand):
    help = "Assign categories to blog posts based on their content"

    def handle(self, *args, **options):
        rules = {
            "Technology": [
                "technology", "tech", "computer", "programming",
                "software", "python", "javascript", "coding",
                "django", "ai", "artificial intelligence"
            ],
            "Lifestyle": [
                "lifestyle", "daily life", "habit", "fashion",
                "wellness", "personal development"
            ],
            "Travel": [
                "travel", "trip", "tourism", "destination",
                "holiday", "vacation"
            ],
            "Food": [
                "food", "recipe", "cooking", "restaurant",
                "briyani", "biryani", "healthy eating"
            ],
            "Health": [
                "health", "fitness", "exercise", "nutrition",
                "mental health", "diet"
            ],
            "Education": [
                "education", "learning", "student", "school",
                "college", "course", "tutorial"
            ],
            "Entertainment": [
                "entertainment", "movie", "music", "film",
                "celebrity", "series"
            ],
            "Business": [
                "business", "marketing", "startup", "finance",
                "entrepreneur", "company"
            ],
            "Sports": [
                "sports", "cricket", "football", "basketball",
                "tennis", "player"
            ],
            "Science": [
                "science", "research", "physics", "biology",
                "chemistry", "space", "experiment"
            ],
        }

        categories = {
            c.name: c for c in category.objects.all()
        }

        general, _ = category.objects.get_or_create(name="General")
        updated = 0

        for post in Post.objects.all():
            text = f"{post.title} {post.content}".lower()
            selected = general

            for category_name, keywords in rules.items():
                if any(keyword in text for keyword in keywords):
                    if category_name in categories:
                        selected = categories[category_name]
                    break

            if post.category_id != selected.id:
                post.category = selected
                post.save(update_fields=["category"])
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Finished. Posts reassigned: {updated}"
            )
        )
