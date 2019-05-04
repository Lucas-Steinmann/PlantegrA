from django.contrib import admin

from plantegra_staff.models import Employee, Team


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('fullname', 'phone_number')


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('ellipsed_memberlist',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Team, TeamAdmin)
