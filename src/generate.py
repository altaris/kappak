#!/usr/bin/env python3

"""Main file."""

import json

from generate_autocompletion import (
    generate_autocompletion
)

from generate_sty import (
    generate_sty
)


PARAMETER_FILE = 'kappak.json'


def main() -> None:
    """Main function."""
    with open(PARAMETER_FILE, 'r') as parameters_file:
        parameters = json.loads(parameters_file.read())
    generate_sty(parameters)
    generate_autocompletion(parameters)


if __name__ == '__main__':
    main()
