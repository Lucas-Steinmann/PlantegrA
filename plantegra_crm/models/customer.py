from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(blank=True)
    contact = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


def get_sentinel_customer() -> Customer:
    """ Returns a user object which can be used instead of a deleted user. """
    return Customer.objects.get_or_create(name='deleted')[0]
