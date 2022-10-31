from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postdata):
        email_check=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['f_n'])<2:
            errors['f_n']="First Name must be longer than 2 characters!"
        if len(postdata['l_n'])<2:
            errors['l_n']="Last Name must be longer than 2 characters!"
        if not email_check.match(postdata['email']): 
            errors['email']="Email mist be valid format"
        if len(postdata['password'])<8:
            errors['password']="Password must be at least 8 chatacters!"
        if postdata['password'] != postdata['confirm_password']:
            errors['confirm_password']="Password and confirm password must match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Response(models.Model):
    text = models.CharField(max_length=255)
    responder = models.ForeignKey(User, related_name="responded_post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="created_post", on_delete=models.CASCADE)
    reply = models.ManyToManyField(Response, null=True, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
