"""Contains doc file generation code."""

from typing import (
    List
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


OUTPUT_DIRECTORY = 'docs/docs'
TEMPLATE_DIRECTORY = 'templates'


class AbstractDocGenerator:

    _parameters: JsonDocument

    def __init__(self, parameters: JsonDocument):
        self._parameters = parameters

    def get_context(self) -> JsonDocument:
        raise NotImplementedError

    def generate(self, template: Template, output_path: str) -> None:
        with open(output_path, 'w') as output_file:
            output_file.write(template.render(self.get_context()))


class EnvironmentsDocGenerator(AbstractDocGenerator):

    def get_context(self) -> JsonDocument:
        return {
            "environments": [{
                "name": env
            } for env in self._parameters["definitions"]
            if self._parameters["definitions"][env]['_type'] == 'env']
        }


class LettersDocGenerator(AbstractDocGenerator):

    def get_context(self) -> JsonDocument:
        return {}


class MathsDocGenerator(AbstractDocGenerator):

    def get_context(self) -> JsonDocument:
        context = {}  # type: JsonDocument
        for definition in self._parameters['definitions']:
            record = self._parameters['definitions'][definition]
            groups = record['doc_group'].split('.')
            if groups[0] != 'maths':
                continue
            maths_group = groups[1] if len(groups) >= 1 else ""
            context[maths_group] = context.get(maths_group, []) + [{
                'name': definition,
                **record
            }]
        return context


class OptionsDocGenerator(AbstractDocGenerator):

    def get_context(self) -> JsonDocument:
        keyval_options = []  # type: List[JsonDocument]
        simple_options = []  # type: List[JsonDocument]

        for option in self._parameters['options']:
            option_definition = self._parameters['options'][option]
            if option_definition['vals']:
                possible_values = ', '.join([
                    f'`{val}`' for val in option_definition['vals']
                ])
                keyval_options += [{
                    'doc': option_definition['doc'],
                    'name': option,
                    'possible_values': possible_values
                }]
            else:
                simple_options += [{
                    'doc': option_definition['doc'],
                    'name': option
                }]

        return {
            'keyval_options': keyval_options,
            'simple_options': simple_options
        }


def generate_doc(parameters: JsonDocument) -> None:
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIRECTORY + '/'),
        lstrip_blocks=True,
        trim_blocks=True
    )
    EnvironmentsDocGenerator(parameters).generate(
        environment.get_template('environments.md'),
        f'{OUTPUT_DIRECTORY}/environments.md'
    )
    LettersDocGenerator(parameters).generate(
        environment.get_template('letters.md'),
        f'{OUTPUT_DIRECTORY}/letters.md'
    )
    MathsDocGenerator(parameters).generate(
        environment.get_template('maths.md'),
        f'{OUTPUT_DIRECTORY}/maths.md'
    )
    OptionsDocGenerator(parameters).generate(
        environment.get_template('options.md'),
        f'{OUTPUT_DIRECTORY}/options.md'
    )