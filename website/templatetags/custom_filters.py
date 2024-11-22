from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Safely get a value from a dictionary."""
    return dictionary.get(key)

@register.filter
def add_class(value, class_name):
    return value.as_widget(attrs={'class': class_name})