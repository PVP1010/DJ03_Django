# Generated by Django 5.1.5 on 2025-02-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_date_news_post_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
    ]
