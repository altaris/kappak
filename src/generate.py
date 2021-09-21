#!/usr/bin/env python3

"""Main file."""

import yaml

from generate_autocompletion import generate_autocompletion
from generate_doc import generate_doc
from generate_sty import generate_sty


PARAMETER_FILE = "kappak.yml"


def main() -> None:
    """Main function."""
    with open(PARAMETER_FILE, "r", encoding="utf-8") as parameters_file:
        parameters = yaml.safe_load(parameters_file.read())
    generate_sty(parameters)
    generate_autocompletion(parameters)
    generate_doc(parameters)


if __name__ == "__main__":
    main()
