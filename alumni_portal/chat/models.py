from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Message(models.Model):
    username = models.CharField(max_length=50)
    room = models.CharField(max_length=20)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.room