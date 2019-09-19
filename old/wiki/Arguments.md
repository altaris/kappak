This page explains argument that can be used while loading the `kappak` package.

# Simple arguments

The name are built on the following simple rule: `+something` adds something, `-something` removes (or doesn't add) something, and `something` changes the behavior of something.

* `+maths`: Defines maths-related commands. This argument is equivalent to all the `+math.*` arguments combined.
* `+maths.arrows`: Mathematical arrows. This argument will be removed soon, use `+maths` instead.
* `+maths.categories`: Commands for category theory. This argument will be removed soon, use `+maths` instead.
* `+maths.characterAccents`: Accents for letters and greek letters. This argument will be removed soon, use `+maths` instead.
* `+maths.characterStyles`: Styles for letters. This argument will be removed soon, use `+maths` instead.
* `+maths.misc`: Miscalenous commands that are maths-related. This argument will be removed soon, use `+maths` instead.
* `+maths.operators`: Mathematical operators. This argument will be removed soon, use `+maths` instead.
* `+maths.theoremEnvs`: Defines the theorem environments.
* `-maths.theoremStyles`: Make all theorem be displayed using the same font. Usually, remarks are italic whereas definitions are bold.
* `-misc`: Removes miscalenous group.
* `+stix`: Includes the `stix` package. Some `stix` command may not be defined as expected, the `kappak` commands having priority. For not, `\barV` is the only such conflict.
* `+tikz`: Declares the `tikz` commands.

# Keyval arguments

For each key, the default value is the first specified.

* `bbStyle` (`normal`, `bbold`): Changes the `mathbb` command.
* `bibliographyStyle` (`plain`, any value for the classical BibTeX `bibliographystyle`): forwards bibliography style.
* `categoryStyle` (`script`, `bf`, `rm`, `sf`, `tt`): Stype to be used for (mathematical) categories.
* `chapterStyle` (`normal`, `cb`, `rb`): Changes the chapter style.
* `headerFooterStyle` (`normal`, `classic`, `cb`, `empty`): Specifies the header and the footer style. If other than `normal`, the `fancyhdr` package will be included.
* `fontSet` (`normal`, `alternate`, `xcharter`): Specifies the font set used.
* `language` (`english`, `french`): Specifies the langage in which the document is written. 
* `lineSpacing` (any decimal number, `1` by default): Specifies the line spacing. Redefines the `baselinestretch` command.
* `margins` (`normal`, `reduced`, `minimal`): Specifies the margins size.
* `scriptStyle` (`normal`, `euler`, `rsfs`, `rsfso`): Specifies which package (none, `eulerscript`, or `mathrsfs`) is to be used for the mathematical script style.
* `titlePageStyle` (`normal`, `classic`, `bar`, `gm`, `gb`): Specifies the title page model.
* `version` (`0406`): Specifies the kappak version to be used.

# Kappak version

The first version of Kappak to introduce versioning is `0406`. There is alias to specifies versions:
* `alpha`: `0407`
* `bellatrix`: `0409`
* `cortana`: `0410`
* `durotan`: `0411`
* `eientei`: `0412`
