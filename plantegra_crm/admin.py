from django.contrib import admin

# Register your models here.
from plantegra_crm.models import Address, Customer, TaskForce
from plantegra_crm.models.appointments import Appointment
from plantegra_crm.models.user import User


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('description', 'customer', 'date_display', 'time_display')


class WorkLocationAddressAdmin(admin.ModelAdmin):
    list_display = ('short_display', 'customer')


class TaskForceAdmin(admin.ModelAdmin):
    model = TaskForce
    list_display = ('working_day', 'ellipsed_member_list', 'appointment_count', 'vehicle')


class AddressInline(admin.TabularInline):
    model = Address

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name in ('street_line1', 'street_line2'):
            field.widget.attrs['style'] = 'width: 20em;'
        elif db_field.name == 'zipcode':
            field.widget.attrs['style'] = 'width: 5em;'
        elif db_field.name == 'city':
            field.widget.attrs['style'] = 'width: 10em;'
        elif db_field.name == 'country':
            field.widget.attrs['style'] = 'width: 2em;'
        elif db_field.name == 'is_invoice':
            field.widget.attrs['style'] = 'width: 2em;'
        return field


class CustomerAdmin(admin.ModelAdmin):
    inlines = (AddressInline,)
    fieldsets = (
        (None, {
            'fields': ('name', 'phone_number', 'contact')
        }),
    )
    list_display = ('name', 'phone_number', 'contact', 'invoice_address')


admin.site.register(User)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(TaskForce, TaskForceAdmin)
