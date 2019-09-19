# How does it work ?

Very well thank you. More precisely, the style and accent related commands are all build on the same scheme :

1. the LaTeX classical backslash,
2. the adequate prefix (see below),
3. the desired character (for instance `A` for small "a", or `KK` for big "K"), or a greek letter.

For instance :

* `\bbRR` produces the black board style "R", commonly used for the set of real numbers ;
* `\bbCC` for the set of complex numbers ;
* `\vecV` for vector "v" ;
* `\hatalpha` for an "alpha" with a hat ;
* `\barH` for a "h" with a bar.

If that is not explicit enough, you can have a look at [this](https://github.com/altaris/kappak/raw/master/test/test.pdf).

# Styles

Enabled with the option `+maths.characterStyles`. The avaible styles are :

* `bb` : black board, it is recommended to use the option `bbStyle=bbold` to use this style on small capped characters ;
* `bf` : bold ;
* `cal` : calligraphy ;
* `frak` : fraktur ;
* `it` : italic ;
* `rm` : roman ;
* `sf` : sans serif.

# Accents

Enabled with the option `+maths.characterAccents`.

* `bar` : overline ;
* `bbar` : two bars ;
* `ch` : check (i.e. reverse hat) ;
* `ddot` : two dots ;
* `dot` : dot ;
* `hat` : hat (duh...) ;
* `o` : a ring ;
* `tild` : tilda ;
* `u` : underline ;
* `uu` : two underlines ;
* `vec` : right arrow.

