Environments
============

All (non `*`) environments are numbered on the same counter. Also, the
environments displayed names are set to the langage specified to kappak (see
the `langage` option).

%{% if target == "higher-structures" %}
**WARNING**: In `kappak-higher-structures`, the `theorem` environment is
replaced by `ktheorem`.
%{% endif %}

The avaible environments are:

{% for environment in environments | sort(attribute='name') %}
* `{{ environment.name }}`
{% endfor %}
