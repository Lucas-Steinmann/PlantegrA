from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from plantegra_staff.models import Employee
from plantegra_staff.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('last_name')
    serializer_class = EmployeeSerializer
    parser_classes = (MultiPartParser,)
