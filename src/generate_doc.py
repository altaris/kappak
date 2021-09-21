"""Contains doc file generation code."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from jinja2 import Environment, FileSystemLoader, Template


OUTPUT_DIRECTORY = "../docs/docs"
TEMPLATE_DIRECTORY = "templates"


class AbstractDocGenerator(ABC):
    """Abstract documentation generator."""

    _parameters: Dict[str, Any]

    def __init__(self, parameters: Dict[str, Any]):
        self._parameters = parameters

    @abstractmethod
    def get_context(self) -> Dict[str, Any]:
        """Returns a Jinja2 context to render the doc template."""

    def generate(self, template: Template, output_path: str) -> None:
        """Renders the documentation template to a file."""
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(template.render(self.get_context()))


class EnvironmentsDocGenerator(AbstractDocGenerator):
    """Documentation generator for the "Environments" page."""

    def get_context(self) -> Dict[str, Any]:
        return {
            "environments": [
                {"name": name}
                for name in self._parameters["definitions"]
                if self._parameters["definitions"][name]["_type"] == "env"
            ]
        }


class LettersDocGenerator(AbstractDocGenerator):
    """Documentation generator for the "Letters" page."""

    def get_context(self) -> Dict[str, Any]:
        return {}


class MathsDocGenerator(AbstractDocGenerator):
    """Documentation generator for the "Maths" page."""

    def get_context(self) -> Dict[str, Any]:
        context = {}  # type: Dict[str, Any]
        for name, record in self._parameters["definitions"].items():
            groups = record["doc_group"].split(".")
            if groups[0] != "maths":
                continue
            maths_group = groups[1] if len(groups) >= 1 else ""
            context[maths_group] = context.get(maths_group, []) + [
                {"name": name, **record}
            ]
        return context


class OptionsDocGenerator(AbstractDocGenerator):
    """Documentation generator for the "Options" page."""

    def get_context(self) -> Dict[str, Any]:
        keyval_options = []  # type: List[Dict[str, Any]]
        simple_options = []  # type: List[Dict[str, Any]]

        for name, record in self._parameters["options"].items():
            if record["vals"]:
                possible_values = ", ".join(
                    [f"`{val}`" for val in record["vals"]]
                )
                keyval_options += [
                    {
                        "doc": record["doc"],
                        "name": name,
                        "possible_values": possible_values,
                    }
                ]
            else:
                simple_options += [{"doc": record["doc"], "name": name}]

        return {
            "keyval_options": keyval_options,
            "simple_options": simple_options,
        }


def generate_doc(parameters: Dict[str, Any]) -> None:
    """Generates all documentation pages."""
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIRECTORY + "/"),
        lstrip_blocks=True,
        trim_blocks=True,
    )
    EnvironmentsDocGenerator(parameters).generate(
        environment.get_template("environments.md"),
        f"{OUTPUT_DIRECTORY}/environments.md",
    )
    LettersDocGenerator(parameters).generate(
        environment.get_template("letters.md"),
        f"{OUTPUT_DIRECTORY}/letters.md",
    )
    MathsDocGenerator(parameters).generate(
        environment.get_template("maths.md"), f"{OUTPUT_DIRECTORY}/maths.md"
    )
    OptionsDocGenerator(parameters).generate(
        environment.get_template("options.md"),
        f"{OUTPUT_DIRECTORY}/options.md",
    )
