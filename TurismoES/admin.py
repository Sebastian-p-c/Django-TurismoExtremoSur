from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'precio', 'descripcion')

admin.site.register(Service, ServiceAdmin)