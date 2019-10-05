import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from plantegra_crm.models import User, Customer, Appointment, Address, TaskForce
from plantegra_crm.serializers import UserSerializer, CustomerSerializer, AppointmentSerializer, \
    AddressSerializer, TaskForceSerializer
from plantegra_staff.serializers import EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows customer to be viewed or edited. """
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer


class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'start_date': ['gt', 'lt']
        }


class AppointmentViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows appointments to be viewed or edited. """
    queryset = Appointment.objects.all().order_by('-start_date')
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppointmentFilter


class AddressViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows work location to be viewed or edited. """
    queryset = Address.objects.all().order_by('zipcode')
    serializer_class = AddressSerializer


class TaskForceFilter(django_filters.FilterSet):
    class Meta:
        model = TaskForce
        fields = {
            'working_day': ['exact']
        }

class TaskForceViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows task forces to be viewed or edited. """
    queryset = TaskForce.objects.all().order_by('-working_day')
    serializer_class = TaskForceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskForceFilter


#class AvailableEmployees(viewsets.ReadOnlyModelViewSet):
#    serializer_class = EmployeeSerializer
#
#    def get_queryset(self):
#        """ Return all employees which have not been """
#        day = self.request.day
#        return free_workers(day)
#
