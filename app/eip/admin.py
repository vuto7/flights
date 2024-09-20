from django.contrib import admin

from .models import Employee, Identity, TimeStamp 

admin.site.register(Employee)
admin.site.register(Identity)
admin.site.register(TimeStamp)
