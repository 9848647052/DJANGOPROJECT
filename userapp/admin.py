from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Farm)
admin.site.register(vegetables)
admin.site.register(customer)
