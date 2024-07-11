from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image/')
    price = models.IntegerField()
    discount = models.IntegerField()
    status = models.BooleanField()


class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=55)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_image/')
    admin = models.CharField(max_length=25)
    date = models.DateField(auto_now=True)


class About(models.Model):
    image = models.ImageField(upload_to='about_image/')
    title = models.CharField(max_length=35)
    describe = models.TextField()
    best = models.CharField(max_length=55)
    works = models.CharField(max_length=255)
    expensice = models.CharField(max_length=255)