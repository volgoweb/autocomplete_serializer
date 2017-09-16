from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=200)
