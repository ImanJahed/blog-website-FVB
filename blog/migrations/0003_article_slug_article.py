# Generated by Django 4.2.3 on 2023-08-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_article_image_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug_article',
            field=models.SlugField(blank=True),
        ),
    ]
