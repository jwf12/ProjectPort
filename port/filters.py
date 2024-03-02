from django import template
import django_filters
from .models import Member

register = template.Library()

@register.filter
def get_item(value, arg):
    return value.get(arg)



class SearchFilter(django_filters.FilterSet):    
    class Meta:
        model = Member
        fields = ['username', 'id']