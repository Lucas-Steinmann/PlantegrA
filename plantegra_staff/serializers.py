from rest_framework import serializers

from plantegra_staff.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'profile_image', 'phone_number', 'user', 'url']
