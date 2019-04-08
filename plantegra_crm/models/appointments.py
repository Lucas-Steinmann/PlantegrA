from django.db import models
from django.utils.translation import gettext_lazy as _

from plantegra_crm.models import WorkLocationAddress
from plantegra_crm.models.customer import Customer


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.ForeignKey(WorkLocationAddress, on_delete=models.CASCADE)
    start_data = models.DateTimeField(verbose_name=_("Start Date"), name="start_date")
    end_data = models.DateTimeField(verbose_name=_("Finish Date"), name="finish_date")
