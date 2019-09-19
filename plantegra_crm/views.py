from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import viewsets, permissions

from plantegra_crm.models import User, Customer, Appointment, Address
from plantegra_crm.serializers import UserSerializer, CustomerSerializer, AppointmentSerializer, \
    AddressSerializer

schema_view = get_schema_view(
    openapi.Info(
        title="PlantegrA API",
        default_version='v1',
        description="The full data access and manipulation API for the PlantegrA CRM/RMS/HR",
        terms_of_service="You are not allowed to use this service.",
        contact=openapi.Contact(email="jonas@integra-lahr.de"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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

