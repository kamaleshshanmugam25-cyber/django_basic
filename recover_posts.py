import os
import django
import sqlite3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from blog.models import Post, category
from django.utils.dateparse import parse_datetime

db = sqlite3.connect("db_backup.sqlite3")
db.row_factory = sqlite3.Row

rows = db.execute(
    "SELECT id, title, content, img_url, created_at, slug FROM blog_post"
).fetchall()

general, _ = category.objects.get_or_create(name="General")
restored = 0

for row in rows:
    if Post.objects.filter(slug=row["slug"]).exists():
        continue

    post = Post(
        title=row["title"],
        content=row["content"],
        img_url=row["img_url"],
        slug=row["slug"],
        category=general,
    )

    created_at = parse_datetime(row["created_at"])
    if created_at:
        post.created_at = created_at

    post.save()
    restored += 1

db.close()

print("Posts found in backup:", len(rows))
print("Posts restored:", restored)
print("Total posts now:", Post.objects.count())
