from django import template

register = template.Library()


@register.filter(name='saludo')
def saludo(value):
    largo = ''
    if len(value) >= 8:
        largo = '<p>Tu nombre es muy largo</p>'
    return "<h1 style='background:green;color:white;'>Bienvendido, {}</h1>{}".format(value,largo)
