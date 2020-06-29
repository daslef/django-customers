import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    note_filter = CharFilter(
        field_name='note',
        lookup_expr='icontains'
        )
    start_date = DateFilter(
        field_name='date_created', 
        lookup_expr='gte'
        )
    end_date = DateFilter(
        field_name='date_created', 
        lookup_expr='lte'
        )
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created', 'note']