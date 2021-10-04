from django.contrib import admin
from .models import Ubicacion, Depto
# Register your models here.

class DeptoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "disponible", "ubicacion"]



admin.site.register(Ubicacion)
admin.site.register(Depto, DeptoAdmin)