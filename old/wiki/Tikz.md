Those command allow to quicly insert commutative diagram made with love and `tikz`. [Here](https://github.com/altaris/kappak/raw/master/test/test.pdf) is an example file.

# Generalities

## Size

Firstly, the command `diagramsize` can be used to specify the size of the diagrams. It takes two arguments, respectively the row separator size and column separator size, both in `em`.

## Styles

Commutative diagram involve arrows. Those can be customized using the `diagramarrows` and `diagramlines` commands, both having 4 arguments. The avaible arrow styles are:
* `` (nothing): accounts for `->`
* `->`: normal
* `<-`: reverse direction
* `<->`
* `->>`
* `<<-`
* `>->`
* `<-<`
* `c->`
* `<-c`: actually a reverse `c->`
* `|->`
* `<-|`

Line styles are:
* `` (nothing): accounts for `-`
* `-`: normal
* `=`: double
* `..`: dotted
* `--`: dashed

Note that styles are persistent. The command `rds` can be used to reset them.

The square diagrams commands take 8 arguments: the first 4 for nodes, and last 4 for arrow labels.
* `squarediagram`: yup, just a square
* `pushoutdiagram`
* `pullbackdiagram`

The triangle diagram commands take 6 arguments: the first 3 for nodes, and the last 3 for arrow labels.
* `triangleULdiagram`: "UL" stand for "Upper Left cornered"
* `triangleURdiagram`: Upper Right
* `triangleDLdiagram`: Down Left (yeah "Lower" would have been more consistent, but "L" was already taken for "Left"...)
* `triangleDRdiagram`: Down Right
* `triangleUdiagram`: Upper
* `triangleLdiagram`: Left
* `triangleRdiagram`: Right
* `triangleDdiagram`: Down

There's also those diagrams, taking 6 arguments: the first 3 for nodes, and the last 3 for arrow labels.
* `eqdiagram`
* `coeqdiagram`
