from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  #auto_now_add cannot update the date posted, better go for creating an argument
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  #if user posted something and later user gets deleted, delete the posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})   #it will return the entire url in reverse based on the given pk value