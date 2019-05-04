from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=100)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=100)
    profile_image = models.ImageField(verbose_name=_("Profile Image"))
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


class Team(models.Model):
    members = models.ManyToManyField(Employee, related_name=_("teams"), verbose_name=_("Team Members"))
