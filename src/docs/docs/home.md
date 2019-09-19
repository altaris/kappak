# What ?

As previously written on the readme file of the repository (have you read it
yet ?), this package regroups functionalities I find useful, from general style
of LaTeX documents (title page, chatper style, header / footer, ...), to more
specific maths related commands (commutative diagrams, category theory, ...).
Consequelty, it might not be as useful for you as it is for me, but you are
welcome to give a try ;)

But what does this package contains ? First of all, it includes common packages
(`babel`, `inputenc`, `ams` stuff, ...) so as to recude your preamble to the
minimum. It provides various ways to quickly modify the look of your document
by passing arguments to the package, so again, minimal code is involved. You'll
find more about that in the Arguments and Styles pages.

Then, the functionnality that started the developpment of this package some
time ago, it offers sorthands for common character styles and accents. I was
extremely tired of repetedly typing `\mathbb{R}` each time I wanted to refer to
real numbers, so I created a specific command for that (namely `\bbRR`).
Nothing too fancy here, everyone does it all the time. Nonetheless, I
generalized this to all letters (including greek letters), and many styles and
accents, in a command name consistent way. You'll find more about that in the
Letters section.

Also, when typesetting mathematical documents, I often needed to define theorem
environments for non ams standard thing, such as `lemma`, `remark`, or
`theorems` (with an "s"). Sometimes, said documents were in english, sometime
in french (yeah I'm french). So I created commands for that too. They are
explained in the Environments section.

Of course, everyone has their shordhands for various mathematical commands.
Mine are documented in the Maths section.

Finally, my studies requires me to draw commutative diagram quite often. I
started using xypic, but I quicky realized that tikz offers a more fancy
rendering. Most of them are quite standard : square, triangular, ... So I
created commands for that too. Now I can draw them in one command call (or up
to three if custom arrows or lines are needed). Refer to Tikz section for more
details.

# Moar & DIY & Contribute

Functionalities come as my needs evolve. And functionalities are present
because I needed them at some point. I try to keep this package as minimal as
possible, hence it happens I remove things. I devoted a file for compatibility
matters, but it's not perfectly working for the moment.

Also, the maths commands present in this package are more related to algebra,
topology and category theory. So depending on which subject you are willing to
typeset using this package, you might find it incomplete for your needs.

So rather that using it out of the box, you might want to consider diging in
the code and reusing some part for your own package. Or use it partially using
arguements, and other packages. Conversely, I, sometime, dig in other's code
and extract cool stuffs for my own package.

Feel free to give me some feedback, waffles, and to signal bugs so I can make
it (the package, we are takling about the package since the beginning of this
file) event better \o/. Also, don't hesitate to send me some cool code snippets
I could incorporate. I'm especially thinking about styles, header / footer, and
title pages.

# Hey I have time to loose :)

Then I suggest you whach Beaking Bad. GREAT show, though a bit slow. Well, slow
is a storytelling style, which is mastered in an astonishing way, in my
opinion. Of course, the actors are incredible. Last but not least, it is a non
negligeable source of internet meme.

# Already whatched it

Then maybe it's time for me to talk about disclaimers. I'll start with the
classical

    This package comes "as is", with no warranty of any kind, and blablabla

Also, as told before, it changes some time. I try to make it retrocompatible so
as to recompile documents I created some time ago. This is achieved trough the
version system (explained in the Arguments section). But then again, it doesn't
perfectly work, and I'm too lazy to look into it when my life doesn't depend on
recompiling a file I crated last year. Seriously though, the package doesn't
change in a major way _that_ often. Nonetheless, let me copypasta :

    This package comes "as is", with no warranty of any kind, and blablabla

Also, I put it (the package) under the
[MIT](http://opensource.org/licenses/MIT) license. Why so ? Because it is
simple and permissive. You can modify, distribute it. You can even use it to
become rich (commercial use, that is). Well that was more an open door for me,
'cause I'd like to become rich, but whatever, it's open for you too. What this
licence also tells is that I cannot be held responsible if you computer takes
fire while compiling this package.