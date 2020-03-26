from django.contrib import admin
from .models import PassModel
# Register your models here.
class PassAdmin(admin.ModelAdmin):
    list_display = ["account", "password","user"]



admin.site.register(PassModel,PassAdmin)