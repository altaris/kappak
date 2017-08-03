kappak
======

# Introduction

This is a homemade LaTeX package regrouping functionalities I deem handy. It is provided under the [MIT](http://opensource.org/licenses/MIT) license.

# Installation

## Linux (texlive)

Execute the following commands in your favorite terminal :

    mkdir -p ~/texmf/tex/latex
    cd ~/texmf/tex/latex
    git clone https://github.com/altaris/kappak.git

## Windows (MiKTex)

Create a folder `this/is/a/path/tex/latex` and clone the repository using git bash :
    
    git clone https://github.com/altaris/kappak.git
    
Alternatively, you can download a zip of this repository, create a folder `this/is/a/path/tex/latex/kappak` and unzip in it.

Lanch the `Settings(Admin)` program. Under the `Roots` tab, add `this/is/a/path`. Under the `General` tab, click on `Refresh FNDB` then on `Update Formats`.

# Autocomplete

The Python script `autocompletion/generate.py` reads through kappak sources and generates autocompletion files.

## In TexMaker

1. TexMaker -> Options -> Settings File -> Save a copy of the settings file.
2. Append the content of the `texmaker-autocompletion.txt` file to the saved TexMaker configuration file, of merge it if the key `Editor\UserCompletion` already exists.
3. TexMaker -> Options -> Settings File -> Replace the settings file by a new one.

## In Sublime-Text

### Linux

Copy `autocompletion/kappak.sublime-completions` in `~/.config/sublime-text-VERSION/Packages/User/`.

### Windows

Copy `autocompletion/kappak.sublime-completions` in `%APPDATA%/Sublime Text 3/Packages`

# [Wiki](https://github.com/altaris/kappak/wiki)