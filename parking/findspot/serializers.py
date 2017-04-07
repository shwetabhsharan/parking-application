from rest_framework import serializers

from findspot.models import Space
class SpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ('id', 'latitude', 'longitude', 'radius', 'is_available', 'booked_for')
