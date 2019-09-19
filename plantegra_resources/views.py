from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from plantegra_resources.models import Vehicle
from plantegra_resources.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.order_by('plate_number')
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser,)

