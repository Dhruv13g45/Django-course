from django.contrib import admin

from .models import FeeStructure, Transaction


admin.site.register(Transaction)
admin.site.register(FeeStructure)