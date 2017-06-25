# -*- coding: utf-8 -*-
from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    cellphone = models.CharField(max_length=20, blank=True)
    biography = models.TextField(blank=True)


class Application(models.Model):
    ACTIVITY_CHOICES = (
            (1, 'Talk'),
            (2, 'Light talk'),
            (3, 'Workshop'),
            (4, 'Keynote')
            )
    speaker = models.ForeignKey('Speaker')
    name = models.CharField(max_length=100)
    activity_type = models.PositiveSmallIntegerField(choices=ACTIVITY_CHOICES)
    description = models.TextField()
    motivation = models.TextField()
    requirements = models.TextField(blank=True)
