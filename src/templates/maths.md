Maths
=====

# Arrows

{% for cmd in arrows | sort(attribute='name') %}
* `{{ cmd.name }}`{% if cmd.argc %}({{ cmd.argc }}){% endif %}{% if cmd.doc %}: {{ cmd.doc }}{% endif %}

{% endfor %}

# Operators

{% for cmd in operators | sort(attribute='name') %}
* `{{ cmd.name }}`{% if cmd.argc %}({{ cmd.argc }}){% endif %}{% if cmd.doc %}: {{ cmd.doc }}{% endif %}

{% endfor %}

# Categories

## Related commands

{% for cmd in categories_commands | sort(attribute='name') %}
* `{{ cmd.name }}`{% if cmd.argc %}({{ cmd.argc }}){% endif %}{% if cmd.doc %}: {{ cmd.doc }}{% endif %}

{% endfor %}

## Predefined categories

{% for cmd in categories_categories | sort(attribute='name') %}
* `{{ cmd.name }}`{% if cmd.argc %}({{ cmd.argc }}){% endif %}{% if cmd.doc %}: {{ cmd.doc }}{% endif %}

{% endfor %}

## Category style

Use prefix `cat`, for letters (any case) only, e.g. `\catCC`.

# Misc

{% for cmd in misc | sort(attribute='name') %}
* `{{ cmd.name }}`{% if cmd.argc %}({{ cmd.argc }}){% endif %}{% if cmd.doc %}: {{ cmd.doc }}{% endif %}

{% endfor %}