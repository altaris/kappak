DIRECTORY = ~/texmf/tex/latex
TARGET    = $(DIRECTORY)/kappak
TEX      = xelatex
TEXFLAGS = -interaction=nonstopmode

autocompletion:
	python3 generate-autocompletion.py
	@echo "Autocompletion files generated. Please refer to README.md for \
	installation instructions."

documentation:
	-mkdir doc
	python3 generate-doc.py
	cd doc && $(TEX) $(TEXFLAGS) kappak.tex && $(TEX) $(TEXFLAGS) kappak.tex

install:
	@mkdir -p $(DIRECTORY)
	@[ -d $(TARGET) ] || ln -s "$(realpath src)" $(TARGET)

uninstall:
	@rm -rf $(TARGET)