#!/usr/bin/python3

import re

# =============================================================================
# Classes
# =============================================================================


class Command:

    def __init__(self, name, argc):
        self.name = name
        try:
            self.argc = int(argc)
        except (ValueError, TypeError):
            self.argc = 0

    def match(line):
        match = re.search(
            r'\\(?:newcommand|newcategory|DeclareMathOperator)' +
            r'\s*\*?\s*\{\\(\w+)\}(?:\[(\d)\])?', line, re.I)
        if match:
            return Command(match.group(1), match.group(2))
        else:
            return None


class Environment(Command):

    def __init__(self, name, argc):
        Command.__init__(self, name, argc)

    def match(line):
        match = re.search(
            r'\\(?:newenvironment|newtheorem)\*?\s*\{(\w+\*?)\}(?:\[(\d)\])?',
            line, re.I)
        if match:
            return Environment(match.group(1), match.group(2))
        else:
            return None

# =============================================================================
# Generators
# =============================================================================


def generateTexmaker(symbols):

    def gen():
        for s in symbols:
            if type(s) == Command:
                yield '\\\\{name}{args}'.format(
                    name = s.name, args = '{\\x2022}' * s.argc)
            elif type(s) == Environment:
                yield '\\\\begin{{{name}}}{args}'.format(
                    name = s.name, args = '{\\x2022}' * s.argc)
                yield '\\\\end{{{name}}}'.format(name = s.name)

    with open('texmaker.txt', 'w', encoding = 'utf-8') as file:
        file.write("Editor\\UserCompletion=" + ", ".join(gen()))


def generateSublime(symbols):

    def placeholder(n):
        return ''.join(('{{${}}}'.format(i + 1) for i in range(n)))

    def gen():
        for s in symbols:
            if type(s) == Command:
                yield '\"\\\\{name}{args}\"'.format(
                    name = s.name, args = placeholder(s.argc))
            elif type(s) == Environment:
                string = "\"\\\\begin{{{name}}}{args}\\n\\t${num}\\n" + \
                    "\\\\end{{{name}}}\""
                yield string.format(
                    name = s.name, args = placeholder(s.argc),
                    num = s.argc + 1)

    with open('kappak.sublime-completions', 'w', encoding = 'utf-8') as file:
        file.write(
            '{{\n\t\"scope\": \"text.tex.latex\",'
            '\n\t\"completions\":\n\t[ {} ]\n}}'.format(", ".join(gen())))


def generateTexstudio(symbols):

    def placeholder(n):
        return ''.join(('{{arg{}%plain}}'.format(i + 1) for i in range(n)))

    def gen():
        for s in symbols:
            if type(s) == Command:
                yield '\\{name}{args}'.format(
                    name = s.name, args = placeholder(s.argc))
            elif type(s) == Environment:
                yield '\\begin{{{name}}}{args}\n\\end{{{name}}}'.format(
                    name = s.name, args = placeholder(s.argc))
                yield '\\end{{{name}}}'.format(name = s.name)

    with open('kappak.cwl', 'w', encoding = 'utf-8') as file:
        file.write('\n'.join(gen()))

# =============================================================================
# Main
# =============================================================================


fileNames = ["kappak.sty"]
targets = [generateTexmaker, generateSublime, generateTexstudio]


def generateSymbols():
    for fn in fileNames:
        with open("src/" + fn, encoding = 'utf-8') as file:
            for line in file:
                for t in [Command, Environment]:
                    c = t.match(line)
                    if c:
                        yield c


if __name__ == "__main__":
    symbols = list(generateSymbols())
    for target in targets:
        target(symbols)