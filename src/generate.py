#!/usr/bin/env python3

"""Main file."""

import json

from generate_autocompletion import (
    generate_autocompletion
)
from generate_doc import (
    generate_doc
)
from generate_sty import (
    generate_sty
)


PARAMETER_FILE = 'kappak.json'


def main() -> None:
    """Main function."""
    with open(PARAMETER_FILE, 'r') as parameters_file:
        parameters = json.loads(parameters_file.read())

    for key in parameters:
        if '_default' not in parameters[key]:
            continue
        default_record = parameters[key].pop('_default')
        for entry in parameters[key]:
            parameters[key][entry] = {
                **default_record, **parameters[key][entry]
            }

    generate_sty(parameters)
    generate_autocompletion(parameters)
    generate_doc(parameters)


if __name__ == '__main__':
    main()
