from django.db import models
from django.db.models import F
from django.utils.text import slugify
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256, blank=True)
    summary = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tags = models.ManyToManyField('Tag', blank=True)
    urls = models.JSONField(null=True, blank=True)
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


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project)

class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    order = models.IntegerField(default=1)
    caption = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    thumb = models.CharField(max_length=256, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [F('order').asc(nulls_last=True)]

    def __str__(self):
        if self.title:
            return f"{str(self.gallery)} - {self.title}"
        else:
            return str(self.gallery)