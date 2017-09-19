import uuid
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


class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)

    @property
    def propname(self):
        return self.title
