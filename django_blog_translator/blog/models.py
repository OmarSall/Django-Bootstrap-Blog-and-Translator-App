from django.db import models
from django.contrib.auth.models import User     #for author field


STATUS = ((0, 'Draft'),(1, 'Published'))
# Create your models here.

#each row in database will be injected in the template

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE) #foreignKey means those data will come from another db table, in this case user db table
    status = models.IntegerField(choices = STATUS, default = 0)  #to distinguish draft posts and published

    def __str__(self):
        return self.title

