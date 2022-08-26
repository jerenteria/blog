from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225, null=True)
    email = models.EmailField()


class Post(models.Model):
    content = models.CharField(max_length=3000, null=True)

