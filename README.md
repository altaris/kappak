kappak
======

# Introduction

This is a homemade LaTeX package regrouping functionalities I deem handy. It is
provided under the [MIT](http://opensource.org/licenses/MIT) license.

# [Documentation](https://altaris.github.io/kappak/)

Reasonably up to date.

# Installation

## Linux

On Linux: execute the following commands in your favorite terminal:

    git clone https://github.com/altaris/kappak.git
    cd kappak
    make install

You're all set!

## Windows

On Winslows: create a folder `this/is/a/path/tex/latex` and clone the
repository using git:

    git clone https://github.com/altaris/kappak.git

Alternatively, you can download a zip of this repository, and extract the
content of `/out/texmf/tex/latex/kappak/` in `this/is/a/path/tex/latex/kappak`.
Then, open the `Settings(Admin)` program. Under the `Roots` tab, add
`this/is/a/path`. Under the `General` tab, click on `Refresh FNDB`, then on
`Update Formats`.

## MacOS

No idea.

# Autocompletion files

## In TeXstudio

* On Linux: copy `out/autocompletion/kappak.cwl` to
  `~/.config/texstudio/completion/user/`;
* On Windows: copy `out/autocompletion/kappak.cwl` to
  `%APPDATA%/TeXstudio/completion/user/`;
* On MacOS: no idea.

## In TexMaker

On all platform:
1. TexMaker -> Options -> Settings File -> Save a copy of the settings file;
2. Append the content of the `out/autocompletion/kappak.texmaker.txt` file to
   the saved TexMaker configuration file, of merge it if the key
   `Editor\UserCompletion` already exists;
3. TexMaker -> Options -> Settings File -> Replace the settings file by a new
   one.

## In Sublime-Text

* On Linux: copy `out/autocompletion/kappak.sublime-completions` to
  `~/.config/sublime-text-<VERSION>/Packages/User/`;
* On Windows: copy `out/autocompletion/kappak.sublime-completions` to
  `%APPDATA%/Sublime Text <VERSION>/Packages/User/`;
* On MacOS: no idea.
