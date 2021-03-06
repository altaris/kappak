"""Contains autocompletion files generation code."""

import json
from typing import (
    List
)

from utils import (
    JsonDocument,
    Record
)


OUTPUT_DIRECTORY = '../out/autocompletion'


class AbstractGenerator:
    """Abstract class representing a autocompletion file generator."""

    _parameters: JsonDocument

    def __init__(self, parameters: JsonDocument):
        self._parameters = parameters

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        raise NotImplementedError

    def generate_record_cmd(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        raise NotImplementedError

    def generate_record_env(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        raise NotImplementedError

    def generate(self, output_file_name: str) -> None:
        """Generates an autocompletion file."""
        completions = []  # type: List[str]
        for definition in self._parameters['definitions']:
            record = self._parameters['definitions'][definition]
            def_type = record.get('_type', None)
            if def_type == 'cmd':
                completions += self.generate_record_cmd(definition, record)
            elif def_type == 'env':
                completions += self.generate_record_env(definition, record)
            else:
                print(f'[WARNING] Unknown record type \"{def_type}\"')
        output_file_path = f'{OUTPUT_DIRECTORY}/{output_file_name}'
        with open(output_file_path, 'w') as output_file:
            print(
                f'[INFO] Generating autocompletion file \"{output_file_path}\"'
            )
            output_file.write(self.generate_file_text(completions))


class SublimeGenerator(AbstractGenerator):
    """Sublime Text autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return json.dumps(
            {"scope": "text.tex.latex", "completions": completions},
            indent=4
        )


    def generate_record_cmd(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        argc = record.get('argc', 0)
        placeholders = [
            '{$' + str(i) + '}' for i in range(1, argc + 1)
        ]
        return ['\\' + name + ''.join(placeholders)]

    def generate_record_env(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return [
            f'\\begin{{name}}\n\t$1\n\\end{{name}}'
        ]


class TexmakerGenerator(AbstractGenerator):
    """TexMaker autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return 'Editor\\UserCompletion=' + ', '.join(completions)

    def generate_record_cmd(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        placeholders = "{\\x2022}" * record.get('argc', 0)
        return ['\\\\' + name + ''.join(placeholders)]

    def generate_record_env(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return [f'\\\\begin{{name}}', f'\\\\end{{name}}']


class TexstudioGenerator(AbstractGenerator):
    """TexStudio autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return '\n'.join(completions)

    def generate_record_cmd(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        argc = record.get('argc', 0)
        placeholders = [
            '{arg' + str(i) + '%plain}' for i in range(1, argc + 1)
        ]
        return ['\\' + name + ''.join(placeholders)]

    def generate_record_env(self, name: str, record: Record) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return [f'\\begin{{name}}', f'\\end{{name}}']


def generate_autocompletion(parameters: JsonDocument) -> None:
    """Entry point."""
    SublimeGenerator(parameters).generate('kappak.sublime-completions')
    TexmakerGenerator(parameters).generate('kappak.texmaker.txt')
    TexstudioGenerator(parameters).generate('kappak.cwl')
