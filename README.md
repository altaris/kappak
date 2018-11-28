kappak
======

# Introduction

This is a homemade LaTeX package regrouping functionalities I deem handy. It is provided under the [MIT](http://opensource.org/licenses/MIT) license.

# [Wiki](https://github.com/altaris/kappak/wiki)

Reasonably:tm: up to date.

# Installation :package:

* On Linux, execute the following commands in your favorite terminal:
```sh
git clone https://github.com/altaris/kappak.git
cd kappak
make install
```
You're all set!

* On Winslows, create a folder `this/is/a/path/tex/latex` and clone the repository using git:
```sh 
git clone https://github.com/altaris/kappak.git
```
Alternatively, you can download a zip of this repository, create a folder `this/is/a/path/tex/latex/kappak` and unzip in it. Then, lanch the `Settings(Admin)` program. Under the `Roots` tab, add `this/is/a/path`. Under the `General` tab, click on `Refresh FNDB` then on `Update Formats`.

# Autocomplete

To generate autocompletion files, run
```sh
make autocompletion
```
and follow the instructions relevant to you.

## In TeXstudio

* On Linux, copy `kappak.cwl` to `~/.config/texstudio/completion/user/`.
* On Windows, copy `kappak.cwl` to `%APPDATA%/TeXstudio/completion/user/`.

## In TexMaker

1. TexMaker -> Options -> Settings File -> Save a copy of the settings file.
2. Append the content of the `texmaker.txt` file to the saved TexMaker configuration file, of merge it if the key `Editor\UserCompletion` already exists.
3. TexMaker -> Options -> Settings File -> Replace the settings file by a new one.

## In Sublime-Text

* On Linux, copy `kappak.sublime-completions` to `~/.config/sublime-text-<VERSION>/Packages/User/`.
* On Windows, copy `kappak.sublime-completions` to `%APPDATA%/Sublime Text <VERSION>/Packages/User/`.

