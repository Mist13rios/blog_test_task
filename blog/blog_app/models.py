from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=64)
    discription = models.CharField(max_length=200)

    def __init__(self):
        return (self.name)

class User(models.Model):
    name = models.CharField(max_length=64)
    main_blog = models.OneToOneField(Blog, on_delete=models.CASCADE,)
    subscripers = models.ManyToManyField(Blog)
    read = models.ManyToManyField(Blog_entry)

    def __init__(self):
        return (self.name)

class Blog_entry(models.Model):
    head = models.CharField(max_length=64)
    text = models.CharField(max_length=8000)
    pub_date = models.DateTimeField('date published')
    blog = models.ForeignKey(Blog)

    def__init__(self):
        return(self.name)
