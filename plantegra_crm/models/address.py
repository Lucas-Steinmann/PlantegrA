from django.db import models
from django.utils.translation import ugettext_lazy as _

from plantegra_crm.models.customer import Customer


class Address(models.Model):
    street_line1 = models.CharField(_('Address 1'), max_length=100, blank=True)
    street_line2 = models.CharField(_('Address 2'), max_length=100, blank=True)
    zipcode = models.CharField(_('ZIP code'), max_length=5, blank=True)
    city = models.CharField(_('City'), max_length=100, blank=True)
    state = models.CharField(_('State'), max_length=100, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)

    def short_display(self):
        return ', '.join(x for x in [self.street_line1, self.street_line2, self.zipcode, self.city] if x)

    def __str__(self):
        return self.short_display()

    class Meta:
        verbose_name_plural = _('Addresses')


class InvoiceAddress(Address):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,
                                 related_name="invoice_address")

    class Meta:
        verbose_name_plural = _('Invoice Addresses')


class WorkLocationAddress(Address):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name="work_locations")

    class Meta:
        verbose_name_plural = _('Work Location Addresses')
