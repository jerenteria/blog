# Generated by Django 3.2.7 on 2023-03-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20230303_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='reply',
        ),
        migrations.AlterField(
            model_name='response',
            name='text',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog_app.post'),
        ),
    ]
