#!/usr/bin/perl

open(IN, "< commands.txt") or die "Couldn't open commands.txt";

my @raw_commands;
while(<IN>) {
	chomp;
	push(@raw_commands, "\\\\" . $_) if($_ =~ /^[\w\d\?\{\}\*]*$/);
}
close IN;

open(TEXMAKER, "> texmaker-autocompletion.txt") or die "Couldn't open texmaker-autocompletion.txt";
my @texmaker_commands = @raw_commands;
s/\?\d*/\{\\x2022\}/g foreach (@texmaker_commands);
print TEXMAKER 'Editor\\UserCompletion=' . join(", ", @texmaker_commands);
close TEXMAKER;

open(SUBLIME, "> kappak.sublime-completions") or die "Could'n open kappak.sublime-completions";
my @sublime_commands = @raw_commands;
foreach (@sublime_commands) {
	s/\?(\d+)/\{\$\1\}/g;
	s/\?/\{\}/g;
	$_ = "\"" . $_ . "\"";
}
print SUBLIME "{\n\t\"scope\": \"text.tex.latex\",\n\t\"completions\":\n\t[ " . join(", ", @sublime_commands) .  " ]\n}";
close SUBLIME