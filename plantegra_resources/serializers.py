from rest_framework import serializers

from plantegra_resources.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'image', 'model', 'plate_number', 'url']
