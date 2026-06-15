import django_filters
from .models import Drink


class DrinkFilter(django_filters.FilterSet):
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Drink
        fields = [
            'max_price',
            'min_price',
            'name',
                  ]
