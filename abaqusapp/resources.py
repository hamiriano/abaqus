from import_export import resources
from .models import Price, Weight

class PriceResource(resources.ModelResource):
    class Meta:
        model = Price

class WeightResource(resources.ModelResource):
    class Meta:
        model = Weight