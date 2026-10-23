
from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post,category
import random


class Command(BaseCommand):
    help = 'Populate and insert data into the database'

    def handle(self, *args: Any, **options: Any):

        Post.objects.all().delete()  # Clear existing data before populating
        
        titles = [
            "My First Blog Post",
            "Exploring Django Models",
            "Understanding Django Views",
            "Django Templates: A Beginner's Guide",
            "Building a Blog with Django",
            "Django Forms: Handling User Input",
            "Django Admin: Customizing the Interface",
            "Django Authentication: User Management",
            "Django REST Framework: Building APIs",
            "Django Deployment: Best Practices",
            "Django Signals: Event Handling",
            "Django Middleware: Request and Response Processing",
            "Django Testing: Writing Unit Tests",
            "Django ORM: Querying the Database",
            "Django Caching: Improving Performance",
            "Django Internationalization: Making Your App Global",
            "Django Security: Protecting Your Application",
            "Django Channels: Real-time Applications",
            "Django Celery: Asynchronous Task Processing",
            "Django Debugging: Tips and Tricks",
            "Django Logging: Monitoring Your Application",
            "Django File Uploads: Handling User Files",
            "Django Pagination: Managing Large Datasets",
        ]

        contents = [
            "This is the content of my first blog post. Welcome to my blog!",
            "In this post, we will explore Django models and how to define them.",
            "Understanding Django views is crucial for building web applications.",
            "Django templates allow you to create dynamic HTML pages easily.",
            "In this tutorial, we will build a simple blog application using Django.",
            "Django forms make it easy to handle user input and validation.",
            "Customizing the Django admin interface can improve your workflow.",
            "Django authentication provides user management features for your application.",
            "Django REST Framework allows you to build powerful APIs quickly.",
            "Learn best practices for deploying your Django application to production.",
            "Django signals allow you to handle events and trigger actions.",
            "Django middleware processes requests and responses.",
            "Writing unit tests helps ensure code quality.",
            "Django ORM provides a powerful way to query the database.",
            "Django caching can improve application performance.",
            "Django internationalization supports a global audience.",
            "Django security features protect against common vulnerabilities.",
            "Django Channels enables real-time applications with WebSockets.",
        ]

        img = [
            f"https://picsum.photos/id/{i}/800/400"
            for i in range(1, 24)
        ]

        categories = category.objects.all()

        for title, content, img_url in zip(titles, contents, img):
            category=random.choice(categories)
            Post.objects.create(
                title=title,
                content=content,
                img_url=img_url,
                category=category,
            )

            


        self.stdout.write(
            self.style.SUCCESS('Data populated successfully!')
        )
