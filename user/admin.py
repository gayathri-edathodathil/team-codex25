from django.contrib import admin
from .models import CustomUser,expenses,tracker
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(expenses)
admin.site.register(tracker)