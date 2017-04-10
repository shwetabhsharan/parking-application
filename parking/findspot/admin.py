# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from findspot.models import Space

class SpaceAdmin(admin.ModelAdmin):

    list_display = ('id', 'latitude', 'longitude', 'radius', 'is_available', 'booked_for', 'booked_at')
    list_filter = ('latitude', 'longitude', 'radius', 'is_available', 'booked_for', 'booked_at')

admin.site.register(Space, SpaceAdmin)
