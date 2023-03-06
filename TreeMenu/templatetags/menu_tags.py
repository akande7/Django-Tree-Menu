from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from TreeMenu.models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def menu(context, parent=None):
    menu_items = MenuItem.objects.filter(parent=parent)

    if not menu_items:
        return ""

    request = context["request"]
    output = "<ul id=list>"

    for item in menu_items:
        url = reverse(item.url_name)
        active = False

        if request.path == url:
            active = True

        output += f'<li>'
        output += f'<a class="{ "active" if active else "unactive" }" href="{url}">{item.title}</a>'
        output += menu(context, parent=item)
        output += "</li>"

    output += "</ul>"

    return mark_safe(output)