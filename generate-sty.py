#!/usr/bin/env python3

from enum import (
    auto,
    Enum,
    unique
)
import json

from jinja2 import Environment, FileSystemLoader


OUTPUT_DIRECTORY = 'texmf/tex/latex/kappak'


@unique
class IncludePolicy(BaseException, Enum):
    DONT_INCLUDE = auto()
    IGNORE = auto()
    INCLUDE = auto()


def check_has_requirements(record: dict, default_record: dict, context: dict):
    requirements = get_value_or_default('requires', record, default_record)
    for requirement in requirements:
        if not context.get(f'pkg_{requirement}', False):
            raise IncludePolicy.DONT_INCLUDE


def check_not_excluded(record: dict, default_record: dict, target: str) -> None:
    exclude_list = get_value_or_default('exclude', record, default_record)
    if target in exclude_list:
        raise IncludePolicy.DONT_INCLUDE


def check_not_special(record_key: str) -> None:
    if record_key.startswith('_'):
        raise IncludePolicy.IGNORE


def datetime() -> str:
    from time import gmtime, strftime
    return strftime("%Y/%m/%d", gmtime())


def main():
    environment = Environment(
        block_end_string='%}',
        block_start_string='%{%',
        comment_end_string='<JINJA2 comment_end_string>',
        comment_start_string='<JINJA2 comment_start_string>',
        line_statement_prefix='<JINJA2 line_statement_prefix>',
        line_comment_prefix='<JINJA2 line_comment_prefix>',
        loader=FileSystemLoader('src/'),
        lstrip_blocks=True,
        trim_blocks=True,
        variable_end_string='%}}',
        variable_start_string='%{{'
    )
    template = environment.get_template('kappak.sty')

    with open('src/kappak.json', 'r') as parameters_file:
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


def get_value_or_default(key: str, data: dict, default_dict: dict):
    if key in data:
        return data[key]
    elif key in default_dict:
        return default_dict[key]
    else:
        print(f'[WARNING] key {key} not found')
        return None


if __name__ == '__main__':
    main()
