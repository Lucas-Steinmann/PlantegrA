from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _

from plantegra_crm.models import Customer


class Address(models.Model):
    street_line1 = models.CharField(_('Address Line 1'), max_length=100, blank=True)
    street_line2 = models.CharField(_('Address Line 2'), max_length=100, blank=True)
    zipcode = models.CharField(_('ZIP code'), max_length=5, blank=True)
    city = models.CharField(_('City'), max_length=100, blank=True)
    state = models.CharField(_('State'), max_length=100, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_invoice = models.BooleanField(_('is invoice address'), default=False)

    def save(self, *args, **kwargs):
        # Check that only one invoice address exists for a given customer
        # If there are others, remove their is_invoice flag.
        # Taken from here: https://stackoverflow.com/a/23513962
        if not self.is_invoice:
            return super().save(*args, **kwargs)
        with transaction.atomic():
            Address.objects.filter(customer=self.customer, is_invoice=True).update(is_invoice=False)
            return super().save(*args, **kwargs)

    def short_display(self):
        return ', '.join(x for x in [self.street_line1, self.street_line2, self.zipcode, self.city] if x)

    def __str__(self):
        return self.short_display()

    class Meta:
        verbose_name_plural = _('Addresses')
