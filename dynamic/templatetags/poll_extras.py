from django import template

register = template.Library()


@register.filter
def spliexc(value):
    return str(value).split('excels/')[1]
