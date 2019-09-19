TEX      = xelatex
TEXFLAGS = -interaction=nonstopmode
BIB      = bibtex
BIBFLAGS = 

all: test.pdf

clean:
	-rm *.aux
	-rm *.bbl
	-rm *.blg
	-rm *.log
	-rm *.out
	-rm *.pdf

%.pdf: %.tex
	$(TEX) $(TEXFLAGS) $<
	$(BIB) $(BIBGLAGS) $(shell basename $< .tex)
	$(TEX) $(TEXFLAGS) $<
	$(TEX) $(TEXFLAGS) $<
