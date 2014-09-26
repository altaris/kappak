#!/usr/bin/perl

open(IN_CMDS, "< commands.txt") or die "Couldn't open commands.txt";
my @raw_cmds;
while(<IN_CMDS>) {
	chomp;
	push(@raw_cmds, "\\\\" . $_) if($_ =~ /^[\w\d\?\{\}\*]+$/);
}
close IN_CMDS;

open(IN_ENVS, "< environments.txt") or die "Couldn't open environments.txt";
my @raw_envs;
while(<IN_ENVS>) {
	chomp;
	push(@raw_envs, $_) if($_ =~ /^[\w\*]+$/);
}
close IN_ENVS;

open(TEXMAKER, "> texmaker-autocompletion.txt") or die "Couldn't open texmaker-autocompletion.txt";
my @texmaker_cmds = @raw_cmds;
s/\?\d*/\{\\x2022\}/g foreach (@texmaker_cmds);
my @texmaker_envs;
foreach (@raw_envs) {
	push(@texmaker_envs, "\\\\begin{" . $_ . "}");
	push(@texmaker_envs, "\\\\end{" . $_ . "}");
}
print TEXMAKER 'Editor\\UserCompletion=' . join(", ", (@texmaker_cmds, @texmaker_envs));
close TEXMAKER;

open(SUBLIME, "> kappak.sublime-completions") or die "Could'n open kappak.sublime-completions";
my @sublime_cmds = @raw_cmds;
foreach (@sublime_cmds) {
	s/\?(\d+)/\{\$\1\}/g;
	s/\?/\{\}/g;
	$_ = "\"" . $_ . "\"";
}
my @sublime_envs = @raw_envs;
$_ = "\"\\\\begin{" . $_ . "}\\n\\t\$1\\n\\\\end{" . $_ . "}\"" foreach (@sublime_envs);
print SUBLIME "{\n\t\"scope\": \"text.tex.latex\",\n\t\"completions\":\n\t[ " . join(", ", (@sublime_cmds, @sublime_envs)) .  " ]\n}";
close SUBLIME