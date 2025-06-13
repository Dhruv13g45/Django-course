from django.contrib import admin

from college_management_system.academics.models import Attendence, Course, Result

# Register your models here.
admin.site.register(Result)
admin.site.register(Attendence)
admin.site.register(Course)