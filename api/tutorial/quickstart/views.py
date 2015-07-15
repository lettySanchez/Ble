from rest_framework import viewsets
from tutorial.quickstart.models import Beacon
from tutorial.quickstart.serializers import BeaconSerializer
from django.conf import settings
dir(settings)
settings.__dict__



class BeaconViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = 'beacon_id'
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer
