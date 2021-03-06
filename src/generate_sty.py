"""Contains sty file generation code."""

from enum import (
    auto,
    Enum,
    unique
)
from time import (
    gmtime,
    strftime
)
from typing import (
    Any
)

from jinja2 import (
    Environment,
    FileSystemLoader,
    Template
)

from utils import (
    JsonDocument,
    Record
)


MAIN_TEMPLATE = 'kappak.sty'
OUTPUT_DIRECTORY = '../out/texmf/tex/latex/kappak'
TEMPLATE_DIRECTORY = 'templates'


@unique
class IncludePolicy(BaseException, Enum):
    """Weather the current record should be included (or excluded, or ignored)
    from the current target."""
    DONT_INCLUDE = auto()
    IGNORE = auto()
    INCLUDE = auto()


def check_has_requirements(record: Record, context: JsonDocument) -> None:
    """Checks if the requirements of a record are all present in the current
    template context."""
    for requirement in record['requires']:
        if not context.get(f'pkg_{requirement}', False):
            raise IncludePolicy.DONT_INCLUDE


def check_not_excluded(record: Record, target: str) -> None:
    """Checks if the current record should be excluded from the target"""
    if target in record['exclude']:
        raise IncludePolicy.DONT_INCLUDE


def datetime() -> str:
    """Gets the current date in YYYY/MM/DD format."""
    return strftime("%Y/%m/%d", gmtime())


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
            check_not_excluded(parameters['packages'][package], target)
            raise IncludePolicy.INCLUDE
        except IncludePolicy as policy:
            if policy == IncludePolicy.DONT_INCLUDE:
                context[f'pkg_{package}'] = False
            elif policy == IncludePolicy.INCLUDE:
                context[f'pkg_{package}'] = True

    for definition in parameters['definitions']:
        def_type = parameters['definitions'][definition].get('_type')
        try:
            record = parameters['definitions'][definition]
            check_not_excluded(record, target)
            check_has_requirements(record, context)
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


def generate_sty(parameters: JsonDocument) -> None:
    """Entry point."""
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
    for target in parameters['targets']:
        generate_target(target, template, parameters)


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
