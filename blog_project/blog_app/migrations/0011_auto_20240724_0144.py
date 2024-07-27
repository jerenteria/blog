# Generated by Django 3.2.7 on 2024-07-24 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20230807_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='reply',
        ),
        migrations.AlterField(
            model_name='response',
            name='responder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responders', to='blog_app.user'),
        ),
    ]