# Generated by Django 3.2.7 on 2022-10-31 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_post_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reply',
        ),
    ]
