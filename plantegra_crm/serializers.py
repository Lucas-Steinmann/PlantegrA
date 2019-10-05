from rest_framework import serializers

from plantegra_crm.models import User, Customer, Appointment, Address, TaskForce


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'contact']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['description', 'location', 'start_date', 'finish_date']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['street_line1', 'street_line2', 'zipcode', 'city', 'state', 'country']


class TaskForceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskForce
        fields = ['members', 'appointments', 'vehicle']
