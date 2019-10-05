from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from plantegra_crm.models import Address, TaskForce


class Appointment(models.Model):
    description = models.CharField(max_length=200, blank=True, default="")
    location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(verbose_name=_("Start Date"), name="start_date")
    finish_date = models.DateTimeField(verbose_name=_("Finish Date"), name="finish_date")
    task_force = models.ForeignKey(TaskForce, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='appointments')

    def clean(self):
        if self.start_date > self.finish_date:
            raise ValidationError(_("Start date of appointment must be earlier than or equal to the finish date."))
        if self.task_force and self.start_date.date() != self.task_force.working_day:
            raise ValidationError(_("All appointments of a task force should be on the day of the task force."))

    def customer(self):
        return _("No customer") if not self.location else self.location.customer

    def date_display(self):
        # TODO: internationalization
        start_date = self.start_date.date().strftime("%d.%m.%Y")
        finish_date = self.finish_date.date().strftime("%d.%m.%Y")
        if self.start_date.date() == self.finish_date.date():
            return start_date
        else:
            return f"{start_date} - {finish_date}"

    def time_display(self):
        start_time = self.start_date.time().strftime("%H:%M")
        finish_time = self.finish_date.time().strftime("%H:%M")
        start_date = self.start_date.date().strftime("%d.%m.%Y")
        finish_date = self.finish_date.date().strftime("%d.%m.%Y")
        if self.start_date.date() == self.finish_date.date():
            return f"{start_time} - {finish_time}"
        else:
            return f"{start_date}T{start_time} - {finish_date}T{finish_time}"  # ISO 8601

    def __str__(self):
        return self.description
