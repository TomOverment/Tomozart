# Generated by Django 5.0.6 on 2024-07-10 18:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_remove_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
