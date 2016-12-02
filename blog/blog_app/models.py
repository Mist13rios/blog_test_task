from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=64)
    discription = models.CharField(max_length=200)

class Blog_entry(models.Model):
    head = models.CharField(max_length=64)
    text = models.CharField(max_length=8000)
    pub_date = models.DateTimeField('date published')
    blog = models.ForeignKey(Blog)

class User(models.Model):
    name = models.CharField(max_length=64)
    subscripers = models.ManyToManyField(Blog)
    read = models.ManyToManyField(Blog_entry)

    def __init(self):
        return [self.name,
            self.subscripers,
            self.read]
