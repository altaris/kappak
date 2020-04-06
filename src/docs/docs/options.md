Options
=======

This page explains options that can be used while loading the `kappak` package.

# Simple options

The name are built on the following simple rule: `+something` adds something,
`-something` removes (or at lease doesn't add) something, and `something`
changes the behavior of something.

* `alpha`: Do not use.
* `bellatrix`: Do not use.
* `cortana`: Do not use.
* `durotan`: Do not use.
* `eientei`: Mandatory.
* `-autopackages`: Tells `kappak` to not automatically include packages.
* `+maths`: Use all maths commands.
* `+maths.arrows`: Use mathematical arrows commands.
* `+maths.categories`: Use category theory commands.
* `+maths.characterAccents`: Use mathematical character accent commands.
* `+maths.characterStyles`: Use mathematical character styles commands.
* `+maths.misc`: Use mathematical miscallenous commands.
* `+maths.operators`: Use mathematical operators commands.
* `+maths.theoremEnvs`: Use theorem environments.
* `-maths.theoremStyles`: Do not use theorem styles for theorem environments.
* `-misc`: Do not use `kappak` miscallenous commands.
* `+stix`: Use `stix`.
* `+tikz`: Use `tikz`.
* `tikz.externalize`: (EXPERIMENTAL) Use `tikz` compilation cache.
* `+xecjk`: Use `xecjk`.


# Keyval options

For each option, the default value is the first specified.

* `bbStyle` (`normal`, `bbold`): Sets the mathematical blackboard letter style.
* `bibliographyStyle` (`_any bibliograph style_`): Sets the bibliography style. Only relevant if you use `kdocument` instead of the standard `document` environment.
* `categoryStyle` (`script`, `allscript`, `bf`, `rm`, `sf`, `tt`): Sets the category style for category theory.
* `chapterStyle` (`normal`, `cb`, `rb`): Sets the chapter style.
* `fontSet` (`normal`, `alternate`, `xcharter`): Sets the font set.
* `headerFooterStyle` (`normal`, `classic`, `cb`, `empty`): Sets the header and footer style.
* `language` (`english`, `french`): Sets the language of the document.
* `lineSpacing` (`_any numerical value_`): Sets the line spacing.
* `margins` (`normal`, `reduced`, `minimal`): Sets the margins.
* `numberTheoremsWithin` (`_any counter, defaults to section_`): What counter theorems should be numbered from.
* `scriptStyle` (`normal`, `euler`, `rsfs`): Sets the mathematical script style.
* `titlePageStyle` (`normal`, `classic`, `bar`, `gm`, `gb`): Sets the title page style.
* `version` (`_any version number_`): Do not use.
