from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Price, Weight
from .resources import PriceResource, WeightResource

@admin.register(Price)
class PriceAdmin(ImportExportModelAdmin):
    resource_class = PriceResource

@admin.register(Weight)
class WeightAdmin(ImportExportModelAdmin):
    resource_class = WeightResource