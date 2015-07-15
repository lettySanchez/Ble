from rest_framework import serializers
from tutorial.quickstart.models import Beacon


class BeaconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beacon
        lookup_field = 'beacon_id'
        fields = ('url', 'beacon_id', 'name', 'last_seen', 'tractor_id',
                  'implement_id', 'longitude', 'latitude')
