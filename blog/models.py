
from django.db import models
from django.utils.text import slugify

class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=100
    )
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "post"
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



