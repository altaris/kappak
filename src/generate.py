#!/usr/bin/env python3

"""Main file."""

from enum import (
    auto,
    Enum,
    unique
)
import json

from jinja2 import Environment, FileSystemLoader


MAIN_TEMPLATE = 'kappak.sty'
OUTPUT_DIRECTORY = '../texmf/tex/latex/kappak'
PARAMETER_FILE = 'kappak.json'
TEMPLATE_DIRECTORY = 'templates'


@unique
class IncludePolicy(BaseException, Enum):
    """Weather the current record should be included (or excluded, or ignored)
    from the current target."""
    DONT_INCLUDE = auto()
    IGNORE = auto()
    INCLUDE = auto()


def check_has_requirements(record: dict, default_record: dict, context: dict):
    """Checks if the requirements of a record are all present in the current
    template context."""
    requirements = get_value_or_default('requires', record, default_record)
    for requirement in requirements:
        if not context.get(f'pkg_{requirement}', False):
            raise IncludePolicy.DONT_INCLUDE


def check_not_excluded(record: dict, default_record: dict, target: str) -> None:
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
    from time import gmtime, strftime
    return strftime("%Y/%m/%d", gmtime())


def main():
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

        package_name = f'kappak-{target}' if target else 'kappak'

        context = {
            'package_name': package_name,
            'date': datetime()
        }

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

        for command in parameters['commands']:
            try:
                check_not_special(command)
                cmd_record = parameters['commands'][command]
                cmd_default = parameters['commands']['_default']
                check_not_excluded(cmd_record, cmd_default, target)
                check_has_requirements(cmd_record, cmd_default, context)
                raise IncludePolicy.INCLUDE
            except IncludePolicy as policy:
                if policy == IncludePolicy.DONT_INCLUDE:
                    context[f'cmd_{command}'] = False
                    print(
                        f'[INFO] Target \"{target}\": excluded command '
                        f'\"{command}\"'
                    )
                elif policy == IncludePolicy.INCLUDE:
                    context[f'cmd_{command}'] = True

        for environment in parameters['environments']:
            try:
                check_not_special(environment)
                env_record = parameters['environments'][environment]
                env_default = parameters['environments']['_default']
                check_not_excluded(env_record, env_default, target)
                check_has_requirements(env_record, env_default, context)
                raise IncludePolicy.INCLUDE
            except IncludePolicy as policy:
                if policy == IncludePolicy.DONT_INCLUDE:
                    context[f'env_{environment}'] = False
                    print(
                        f'[INFO] Target \"{target}\": excluded environment '
                        f'\"{environment}\"'
                    )
                elif policy == IncludePolicy.INCLUDE:
                    context[f'env_{environment}'] = True

        output_file_path = f'{OUTPUT_DIRECTORY}/{package_name}.sty'
        with open(f'{output_file_path}', 'w') as output_file:
            print(
                f'[INFO] Rendering target \"{target}\" to '
                f'\"{output_file_path}\"'
            )
            output_file.write(template.render(context))


def get_value_or_default(key: str, record: dict, default_record: dict):
    """Gets a value from a record, or a provided default record."""
    if key in record:
        return record[key]
    elif key in default_record:
        return default_record[key]
    else:
        print(f'[WARNING] Key {key} not found')
        return None


if __name__ == '__main__':
    main()
