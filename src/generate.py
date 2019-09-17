#!/usr/bin/env python3

"""Main file."""

from enum import (
    auto,
    Enum,
    unique
)
import json
from time import (
    gmtime,
    strftime
)
from typing import (
    Any,
    Dict
)

from jinja2 import (
    Environment,
    FileSystemLoader,
    Template
)


MAIN_TEMPLATE = 'kappak.sty'
OUTPUT_DIRECTORY = '../texmf/tex/latex/kappak'
PARAMETER_FILE = 'kappak.json'
TEMPLATE_DIRECTORY = 'templates'


JsonDocument = Dict[str, Any]  # pylint: disable=invalid-name
Record = Dict[str, Any]  # pylint: disable=invalid-name


@unique
class IncludePolicy(BaseException, Enum):
    """Weather the current record should be included (or excluded, or ignored)
    from the current target."""
    DONT_INCLUDE = auto()
    IGNORE = auto()
    INCLUDE = auto()


def check_has_requirements(
        record: Record,
        default_record: Record,
        context: JsonDocument
    ) -> None:
    """Checks if the requirements of a record are all present in the current
    template context."""
    requirements = get_value_or_default('requires', record, default_record)
    for requirement in requirements:
        if not context.get(f'pkg_{requirement}', False):
            raise IncludePolicy.DONT_INCLUDE


def check_not_excluded(
        record: Record,
        default_record: Record,
        target: str
    ) -> None:
    """Checks if the current record should be excluded from the target"""
    exclude_list = get_value_or_default('exclude', record, default_record)
    if target in exclude_list:
        raise IncludePolicy.DONT_INCLUDE


def check_not_special(record_key: str) -> None:
    """Checks if the current record is a special one, i.e. if its name starts with an underscore."""
    if record_key.startswith('_'):
        raise IncludePolicy.IGNORE


def datetime() -> str:
    """Gets the current date in YYYY/MM/DD format."""
    return strftime("%Y/%m/%d", gmtime())


def main() -> None:
    """Main function."""
    environment = Environment(
        block_end_string='%}',
        block_start_string='%{%',
        comment_end_string='<JINJA2 comment_end_string>',
        comment_start_string='<JINJA2 comment_start_string>',
        line_statement_prefix='<JINJA2 line_statement_prefix>',
        line_comment_prefix='<JINJA2 line_comment_prefix>',
        loader=FileSystemLoader(TEMPLATE_DIRECTORY + '/'),
        lstrip_blocks=True,
        trim_blocks=True,
        variable_end_string='%}}',
        variable_start_string='%{{'
    )
    template = environment.get_template(MAIN_TEMPLATE)

    with open(PARAMETER_FILE, 'r') as parameters_file:
        parameters = json.loads(parameters_file.read())

    for target in parameters['targets']:
        generate_target(target, template, parameters)


def generate_target(
        target: str,
        template: Template,
        parameters: JsonDocument
    ) -> None:
    """Generate the sty file for a given target."""
    package_name = f'kappak-{target}' if target else 'kappak'
    context = {
        'package_name': package_name,
        'date': datetime()
    }  # type: JsonDocument

    for package in parameters['packages']:
        try:
            check_not_special(package)
            check_not_excluded(
                parameters['packages'][package],
                parameters['packages']['_default'],
                target
            )
            raise IncludePolicy.INCLUDE
        except IncludePolicy as policy:
            if policy == IncludePolicy.DONT_INCLUDE:
                context[f'pkg_{package}'] = False
            elif policy == IncludePolicy.INCLUDE:
                context[f'pkg_{package}'] = True

    for definition in parameters['definitions']:
        def_type = parameters['definitions'].get('_type')
        try:
            check_not_special(definition)
            def_record = parameters['definitions'][definition]
            def_default = parameters['definitions']['_default']
            check_not_excluded(def_record, def_default, target)
            check_has_requirements(def_record, def_default, context)
            raise IncludePolicy.INCLUDE
        except IncludePolicy as policy:
            if policy == IncludePolicy.DONT_INCLUDE:
                context[f'{def_type}_{definition}'] = False
                print(
                    f'[INFO] Target \"{target}\": excluded definition '
                    f'\"{definition}\"'
                )
            elif policy == IncludePolicy.INCLUDE:
                context[f'{def_type}_{definition}'] = True

    output_file_path = f'{OUTPUT_DIRECTORY}/{package_name}.sty'
    with open(f'{output_file_path}', 'w') as output_file:
        output_file.write(template.render(context))

    print(f'[INFO] Generated target \"{target}\" to \"{output_file_path}\"')


def get_value_or_default(
        key: str,
        record: Record,
        default_record: Record
    ) -> Any:
    """Gets a value from a record, or a provided default record."""
    if key in record:
        return record[key]
    if key in default_record:
        return default_record[key]
    print(f'[WARNING] Key {key} not found')
    return None


if __name__ == '__main__':
    main()
