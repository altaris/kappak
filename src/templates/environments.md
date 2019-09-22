Environments
============

All (non `*`) environments are numbered on the same counter. Also, the
environments displayed names are set to the langage specified to kappak (see
the `langage` option).

The avaible environments are:

{% for environment in environments | sort(attribute='name') %}
* `{{ environment.name }}`
{% endfor %}
