from django.contrib import admin

# Register your models here.
from job.models import JobOpportunity
from user.models import User, EmployeeProfile, EmployerProfile, WorkSchedule

admin.site.register(User)
admin.site.register(EmployeeProfile)
admin.site.register(EmployerProfile)
admin.site.register(WorkSchedule)
admin.site.register(JobOpportunity)

