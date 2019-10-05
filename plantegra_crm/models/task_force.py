from datetime import date

from django.db import models
from django.db.models import ManyToManyField, ForeignKey, DateField, QuerySet
from django.utils.translation import gettext_lazy as _

from plantegra_resources.models import Vehicle
from plantegra_staff.models import Employee


def free_workers(day: date) -> QuerySet:
    return Employee.objects.difference(busy_workers(day))


def busy_workers(day: date) -> QuerySet:
    return Employee.objects.filter(taskforce__working_day__day=day)


class TaskForce(models.Model):
    """
    A task force is a group of employees which work together on multiple appointments on a single day.
    """
    members = ManyToManyField(Employee, verbose_name=_("Members"))
    vehicle = ForeignKey(Vehicle, verbose_name=_("Vehicle"), on_delete=models.SET_NULL, null=True, blank=True)
    # This is the date at which the task force operates.
    # This field could be derived from the dates of the appointments.
    # But we opted to adding this field for two reasons:
    #  1. Decrease validation and query complexity, e.g. get all task forces of a day
    #  2. (and more important) be able to have task forces without appointments (and still have a valid date)
    working_day = DateField(verbose_name=_("Date of deployment"), default=date.today)

    @property
    def ellipsed_member_list(self):
        return ellipse(', '.join([m.fullname for m in self.members.all()]), 100)

    @property
    def appointment_count(self):
        return len(self.appointments.all())

    # It would be nice if we could validate here
    # if a member was added to more than one task
    # force on a given day. But this is not possible,
    # since validate_unique is called before the model is save
    # This means accessing the ManyToManyField is not possible.
    # See: https://stackoverflow.com/a/7986937
    #def validate_unique(self, exclude=None):
    #    super().validate_unique(exclude)
    #    if (0 != self.members
    #                 .values_list('taskforce', flat=True)
    #                 .exclude(taskforce=self)
    #                 .filter(taskforce__working_day=self.working_day)
    #                 .count()):
    #        raise ValidationError(_("Employee can only be in one task force on a given day."))

    def __str__(self):
        return self.ellipsed_member_list


def ellipse(string, length):
    return string[:length-3] + '...' if len(string) > length else string
