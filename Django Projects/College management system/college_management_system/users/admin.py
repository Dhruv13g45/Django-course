from django.contrib import admin

from college_management_system.users.models import StudentProfile, TeacherProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
