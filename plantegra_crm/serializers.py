from rest_framework import serializers

from plantegra_crm.models import User, Customer, Appointment, Address, TaskForce


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'url']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_number', 'contact', 'url']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'description', 'location', 'start_date', 'finish_date', 'url']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_line1', 'street_line2', 'zipcode', 'city', 'state', 'country', 'url']


class TaskForceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskForce
        fields = ['id', 'members', 'appointments', 'vehicle', 'working_day', 'url']
