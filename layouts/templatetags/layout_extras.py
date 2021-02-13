from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    if 'Price' in key:
        return round(dictionary.get(key), 2)
    if 'Volume' in key:
        return "{:,}".format(round(dictionary.get(key)))
    return dictionary.get(key)