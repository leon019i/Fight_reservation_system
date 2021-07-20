import django_filters
from django_filters import IsoDateTimeFilter

from .models import add_flight


class add_flightFilter(django_filters.FilterSet):
    source = django_filters.CharFilter(field_name='source', lookup_expr='icontains', label="Source")
    To = django_filters.CharFilter(field_name='To', lookup_expr='icontains', label="TO")
    check_in_date = django_filters.DateFilter(field_name='check_in_date', lookup_expr='icontains',
                                              label="check in date ")
    check_out_date = django_filters.DateFilter(field_name='check_out_date', lookup_expr='icontains',
                                               label="Check out date")
    no_of_tickets = django_filters.NumberFilter(field_name='no_of_tickets', lookup_expr='icontains',label="No of tickets")


class Meta:
    models = add_flight
    fields = ['check_in_date']
