from django.db import models
from django.utils.translation import gettext_lazy as _


class Resource(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(verbose_name=_("Image"), blank=True, null=True)

    def __str__(self):
        return self.name


class Vehicle(Resource):
    model = models.CharField(verbose_name=_("Vehicle Model"), max_length=200)
    plate_number = models.CharField(verbose_name=_("Plate number"), max_length=20)
