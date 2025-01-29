from django.contrib import admin
from .models import Parcel 

class ParcelAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "item", "count", "cost", "taken", "receiveDate"]

# Register your models here.
admin.site.register(Parcel, ParcelAdmin)