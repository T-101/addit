import random

from uuid import uuid4

from django.db import models
from django_extensions.db.fields import AutoSlugField


class VisibleQuotes(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Quote(models.Model):
    time_added = models.DateTimeField()
    handle = models.CharField(max_length=16)
    topic = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=["topic"])
    content = models.TextField(max_length=512)
    uuid = models.UUIDField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    objects = models.Manager()
    visible = VisibleQuotes()

    def get_random_quote(self, query=None):
        items = self.__class__.visible.all()
        if query:
            items = items.filter(topic__icontains=query)
        return random.choice(items)

    def filter_by_topic(self, search):
        return self.__class__.visible.filter(topic__icontains=search)

    def filter_by_content(self, search):
        return self.__class__.visible.filter(content__icontains=search)

    def filter_by_handle(self, search):
        return self.__class__.visible.filter(handle__icontains=search)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid4())
            while self.__class__.objects.filter(uuid=self.uuid).exists():
                self.uuid = str(uuid4())
        super().save(*args, **kwargs)
