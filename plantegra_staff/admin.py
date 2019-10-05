from django.contrib import admin

from plantegra_staff.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('fullname', 'phone_number')


admin.site.register(Employee, EmployeeAdmin)
