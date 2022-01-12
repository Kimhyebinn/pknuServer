import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"] # nl2br: 줄바꿈 태그를 br 태그로 바꿈.
    return mark_safe(markdown.markdown(value, extensions=extensions))