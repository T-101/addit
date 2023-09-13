import re

from django import template

register = template.Library()


@register.filter
def parse_quote(val):
    ret = re.sub(r"<3", r"&hearts;", val)
    ret = re.sub(r"(\[?\d?\d?:?\d?\d?\]?\s?)(<.*?>)", r"\n\1\2", ret)
    ret = re.sub(r"<", "&lt;", ret)
    ret = re.sub(r">", "&gt;", ret)
    ret = re.sub(r"(&lt;.*?&gt;)", r'<strong>\1</strong>', ret)
    ret = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', ret)
    ret = re.sub(r"&hearts;", r'<i class="fa-solid fa-heart"></i>', ret)
    return ret.strip()
