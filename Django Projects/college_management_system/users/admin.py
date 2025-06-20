from django.contrib import admin

from .models import FeeManager, Librarian, StudentProfile, TeacherProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Librarian)
admin.site.register(FeeManager)