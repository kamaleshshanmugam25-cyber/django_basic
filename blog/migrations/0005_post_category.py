
import django.db.models.deletion
from django.db import migrations, models


def create_default_category(apps, schema_editor):
    Category = apps.get_model('blog', 'category')
    Category.objects.using(
        schema_editor.connection.alias
    ).get_or_create(
        id=1,
        defaults={'name': 'General'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_alter_post_slug'),
    ]

    operations = [
        migrations.RunPython(
            create_default_category,
            migrations.RunPython.noop,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='blog.category',
            ),
            preserve_default=False,
        ),
    ]
