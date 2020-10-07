from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    summary=models.TextField()

    def __str__(self):
        return self.title



#username:vijay
#password:onetwo@
#password:Onetwo@@