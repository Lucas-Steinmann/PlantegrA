from rest_framework import serializers

from plantegra_staff.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'profile_image', 'phone_number', 'user']
