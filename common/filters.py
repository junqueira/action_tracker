from django.template.defaultfilters import register

@register.filter(name='get_selected_choice')
def get_selected_choice(choices,value):
    for choice in choices:
        choice_value = choice [ 0 ]
        choice_text  = choice [ 1 ]

        if choice_value == value:
            return choice_text

    return ""

@register.filter(name='endswith')
def endswith(value, s):
    return value.endswith(s)
