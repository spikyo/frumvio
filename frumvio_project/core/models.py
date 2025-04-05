from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, IntegerField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Topic(Model):
    title = CharField(max_length=255)
    description = TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(to='User', on_delete=CASCADE)
    
    def __str__(self):
        return self.title


class Post(Model):
    body = TextField()
    created_at = DateTimeField(auto_now_add=True)
    topic = ForeignKey(to=Topic, on_delete=CASCADE)
    created_by = ForeignKey(to='User', on_delete=CASCADE)
    
    def __str__(self):
        return self.body[:30]
