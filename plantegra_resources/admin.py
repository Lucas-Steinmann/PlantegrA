from django.contrib import admin

from plantegra_resources.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    admin = Vehicle
    list_display = ('name', 'model', 'plate_number')


admin.site.register(Vehicle, VehicleAdmin)
