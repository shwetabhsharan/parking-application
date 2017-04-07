# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework.exceptions import ValidationError

# Create your models here.
class Space(models.Model):
    """
        Parking space metadata
    """

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    radius = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    booked_for = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.booked_for > 60 or self.booked_for < 0:
            raise ValidationError('Parking slots can only be used for 1 min to 60 minutes')
        super(Space, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Parking Space Metadata'
        verbose_name_plural = 'Parking Space Metadata'
