from django import template


register = template.Library()

@register.filter(name='transaction_value')
def transaction_value(value):
    try:
        val = int(value)
    except ValueError:
        val = 0
    try:
        val = float(value)
    except ValueError:
        val = 0
    return val