
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(
                default='',
                max_length=100,
                blank=True,
            ),
        ),
    ]
