from django.db import models

import re

# Create your models here.
class Kind(models.Model):
    name = models.CharField(max_length = 140)
    specification = models.TextField()
    first_aid = models.TextField()
    image_path = models.TextField()
    def __unicode__(self):
        return self.name

    def kind_thumbnail(self):
        return '<img src="%s" width="150" height="120"/>' % self.image_path
    kind_thumbnail.allow_tags = True

    def name_separated(self):
        name_sep = re.sub(r"(?<=\w)([A-Z])", r" \1", self.name)
        return name_sep

class Snake(models.Model):
    name = models.CharField(max_length = 140)
    #specification = models.TextField()
    #first_aid = models.TextField()
    image_path = models.TextField()
    location = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __unicode__(self):
        return self.name

    def dump(self):
        return {"snakelist": {'name': self.name,
                              'latitude': self.latitude,
                              'longitude': self.longitude}}

    def snake_thumbnail(self):
        return '<img src="%s" width="150" height="120"/>' % self.image_path
    snake_thumbnail.allow_tags = True

    @property
    def name_separated(self):
        name_sep = re.sub(r"(?<=\w)([A-Z])", r" \1", self.name)
        return name_sep

    @property
    def kind_image_path(self):
        object = Kind.objects.filter(name = self.name)
        for e in object:
            e =e
        return e.image_path

    @property
    def specification(self):
        object = Kind.objects.filter(name = self.name)
        for e in object:
            e =e
        return e.specification

    @property
    def first_aid(self):
        object = Kind.objects.filter(name = self.name)
        for e in object:
            e =e
        return e.first_aid

    @property
    def count_snake(self):
        count = Snake.objects.all().count()
        
        return count