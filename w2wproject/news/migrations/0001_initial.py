# Generated by Django 5.0.6 on 2024-06-19 14:04

import news.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('avatar_id', models.ImageField(blank=True, null=True, upload_to=news.models.get_image_path_brand, verbose_name='Аватар')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на пост')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
