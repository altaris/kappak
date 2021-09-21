"""Contains sty file generation code."""

from enum import auto, Enum, unique
from time import gmtime, strftime
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, Template


MAIN_TEMPLATE = "kappak.sty"
OUTPUT_DIRECTORY = "../out/texmf/tex/latex/kappak"
TEMPLATE_DIRECTORY = "templates"


@unique
class IncludePolicy(BaseException, Enum):
    """
    Weather the current record should be included (or excluded, or ignored)
    from the current target.
    """

    DONT_INCLUDE = auto()
    IGNORE = auto()
    INCLUDE = auto()


def check_has_requirements(
    record: Dict[str, Any], context: Dict[str, Any]
) -> None:
    """
    Checks if the requirements of a record are all present in the current
    template context.
    """
    for requirement in record["requires"]:
        if not context.get(f"pkg_{requirement}", False):
            raise IncludePolicy.DONT_INCLUDE


def check_not_excluded(record: Dict[str, Any], target: str) -> None:
    """Checks if the current record should be excluded from the target."""
    if target in record["exclude"]:
        raise IncludePolicy.DONT_INCLUDE


def generate_target(
    target: str, template: Template, parameters: Dict[str, Any]
) -> None:
    """Generate the sty file for a given target."""
    package_name = f"kappak-{target}" if target else "kappak"
    context = {
        "package_name": package_name,
        "date": strftime("%Y/%m/%d", gmtime()),
    }  # type: Dict[str, Any]

    for name, record in parameters["packages"].items():
        try:
            check_not_excluded(record, target)
            raise IncludePolicy.INCLUDE
        except IncludePolicy as policy:
            if policy == IncludePolicy.DONT_INCLUDE:
                context[f"pkg_{name}"] = False
            elif policy == IncludePolicy.INCLUDE:
                context[f"pkg_{name}"] = True

    for name, record in parameters["definitions"].items():
        def_type = record.get("_type")
        try:
            check_not_excluded(record, target)
            check_has_requirements(record, context)
            raise IncludePolicy.INCLUDE
        except IncludePolicy as policy:
            if policy == IncludePolicy.DONT_INCLUDE:
                context[f"{def_type}_{name}"] = False
                print(
                    f"[INFO] Target '{target}': excluded definition "
                    f"'{name}'"
                )
            elif policy == IncludePolicy.INCLUDE:
                context[f"{def_type}_{name}"] = True

    output_file_path = f"{OUTPUT_DIRECTORY}/{package_name}.sty"
    with open(f"{output_file_path}", "w", encoding="utf-8") as output_file:
        output_file.write(template.render(context))

    print(f"[INFO] Generated target '{target}' to '{output_file_path}'")


def generate_sty(parameters: Dict[str, Any]) -> None:
    """Main method."""
    environment = Environment(
        block_end_string="%}",
        block_start_string="%{%",
        comment_end_string="<JINJA2 comment_end_string>",
        comment_start_string="<JINJA2 comment_start_string>",
        line_statement_prefix="<JINJA2 line_statement_prefix>",
        line_comment_prefix="<JINJA2 line_comment_prefix>",
        loader=FileSystemLoader(TEMPLATE_DIRECTORY + "/"),
        lstrip_blocks=True,
        trim_blocks=True,
        variable_end_string="%}}",
        variable_start_string="%{{",
    )
    template = environment.get_template(MAIN_TEMPLATE)
    for target in parameters["targets"]:
        generate_target(target, template, parameters)
