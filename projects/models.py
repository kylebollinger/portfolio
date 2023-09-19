from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tags = models.ManyToManyField('Tag', blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title and len(self.title) > 0:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and len(self.name) > 0:
            self.name = self.name.lower().strip()
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)