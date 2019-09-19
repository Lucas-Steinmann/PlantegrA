from rest_framework import serializers

from plantegra_resources.models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['name', 'image', 'model', 'plate_number']
