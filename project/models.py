from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)

    @property
    def propname(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    @property
    def propname(self):
        return self.name
