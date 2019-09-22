Options
=======

This page explains options that can be used while loading the `kappak` package.

# Simple options

The name are built on the following simple rule: `+something` adds something,
`-something` removes (or at lease doesn't add) something, and `something`
changes the behavior of something.

{% for option in simple_options %}
* `{{ option.name }}`: {{ option.doc }}
{% endfor %}


# Keyval options

For each option, the default value is the first specified.

{% for option in keyval_options %}
* `{{ option.name }}` ({{ option.possible_values }}): {{ option.doc }}
{% endfor %}
