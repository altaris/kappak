USER_LATEX_DIR 		= ~/texmf/tex/latex
USER_KAPPAK_DIR   	= $(USER_LATEX_DIR)/kappak

LOCAL_LATEX_DIR  	= out/texmf/tex/latex
LOCAL_KAPPAK_DIR  	= $(LOCAL_LATEX_DIR)/kappak

TEX      			= xelatex
TEXFLAGS 			= -interaction=nonstopmode

autocompletion:
	python3 generate-autocompletion.py
	@echo "Autocompletion files generated. Please refer to README.md for \
	installation instructions."

check:
	mypy src/*.py

clean:
	rm $(LOCAL_KAPPAK_DIR)/*.sty

documentation:
	-mkdir doc
	python3 generate-doc.py
	cd doc &&								\
		$(TEX) $(TEXFLAGS) kappak.tex &&	\
		$(TEX) $(TEXFLAGS) kappak.tex

generate:
	cd src/ && python3 generate.py

install: uninstall
	mkdir -p $(USER_LATEX_DIR) &&	\
		ln -s "$(realpath $(LOCAL_KAPPAK_DIR))" $(USER_KAPPAK_DIR)

uninstall:
	-rm -rf $(USER_KAPPAK_DIR)
