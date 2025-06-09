from django.db import models

# Create your models here.
# ORM - Object Relational Mapping
# ORM helps to map a python object to database instance


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
