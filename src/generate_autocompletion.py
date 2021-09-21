"""Contains autocompletion files generation code."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import json


OUTPUT_DIRECTORY = "../out/autocompletion"


class AbstractGenerator(ABC):
    """Abstract class representing a autocompletion file generator."""

    _parameters: Dict[str, Any]

    def __init__(self, parameters: Dict[str, Any]):
        self._parameters = parameters

    @abstractmethod
    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""

    @abstractmethod
    def generate_record_cmd(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""

    @abstractmethod
    def generate_record_env(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a env record."""

    def generate(self, output_file_name: str) -> None:
        """Generates an autocompletion file."""
        completions = []  # type: List[str]
        for name, record in self._parameters["definitions"].items():
            def_type = record.get("_type", None)
            if not def_type:
                pass
            elif def_type == "cmd":
                completions += self.generate_record_cmd(name, record)
            elif def_type == "env":
                completions += self.generate_record_env(name, record)
            else:
                print(f"[WARNING] Unknown record type '{def_type}'")
        output_file_path = f"{OUTPUT_DIRECTORY}/{output_file_name}"
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            print(
                f"[INFO] Generating autocompletion file '{output_file_path}'"
            )
            output_file.write(self.generate_file_text(completions))


class SublimeGenerator(AbstractGenerator):
    """Sublime Text autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return json.dumps(
            {"scope": "text.tex.latex", "completions": completions},
            indent=4,
        )

    def generate_record_cmd(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        argc = record.get("argc", 0)
        placeholders = ["{$" + str(i) + "}" for i in range(1, argc + 1)]
        return ["\\" + name + "".join(placeholders)]

    def generate_record_env(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return ["\\begin{" + name + "}\n\t$1\n\\end{" + name + "}"]


class TexmakerGenerator(AbstractGenerator):
    """TexMaker autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return "Editor\\UserCompletion=" + ", ".join(completions)

    def generate_record_cmd(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        placeholders = "{\\x2022}" * record.get("argc", 0)
        return ["\\\\" + name + "".join(placeholders)]

    def generate_record_env(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return ["\\\\begin{" + name + "}", "\\\\end{" + name + "}"]


class TexstudioGenerator(AbstractGenerator):
    """TexStudio autocompletion file generator."""

    def generate_file_text(self, completions: List[str]) -> str:
        """Generates the autocompletion file content from its entry list."""
        return "\n".join(completions)

    def generate_record_cmd(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a cmd record."""
        argc = record.get("argc", 0)
        placeholders = [
            "{arg" + str(i) + "%plain}" for i in range(1, argc + 1)
        ]
        return ["\\" + name + "".join(placeholders)]

    def generate_record_env(
        self, name: str, record: Dict[str, Any]
    ) -> List[str]:
        """Generates one or multiple completion entries from a env record."""
        return ["\\begin{" + name + "}", "\\end{" + name + "}"]


def generate_autocompletion(parameters: Dict[str, Any]) -> None:
    """Entry point."""
    SublimeGenerator(parameters).generate("kappak.sublime-completions")
    TexmakerGenerator(parameters).generate("kappak.texmaker.txt")
    TexstudioGenerator(parameters).generate("kappak.cwl")
