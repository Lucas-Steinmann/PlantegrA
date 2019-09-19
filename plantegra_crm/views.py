from rest_framework import viewsets

from plantegra_crm.models import User, Customer, Appointment, Address
from plantegra_crm.serializers import UserSerializer, CustomerSerializer, AppointmentSerializer, \
    AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows customer to be viewed or edited. """
    queryset = Customer.objects.all().order_by('-name')
    serializer_class = CustomerSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows appointments to be viewed or edited. """
    queryset = Appointment.objects.all().order_by('-start_date')
    serializer_class = AppointmentSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows work location to be viewed or edited. """
    queryset = Address.objects.all().order_by('-zipcode')
    serializer_class = AddressSerializer

