from django import template
import json

register = template.Library()

@register.filter
def queryset_to_json(queryset):
    return json.dumps(list(queryset.values()))