# Generated by Django 5.1.5 on 2025-02-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news_post',
            name='content',
            field=models.TextField(verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
