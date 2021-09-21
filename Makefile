USER_LATEX_DIR 		= ~/texmf/tex/latex
USER_KAPPAK_DIR   	= $(USER_LATEX_DIR)/kappak

LOCAL_LATEX_DIR  	= out/texmf/tex/latex
LOCAL_KAPPAK_DIR  	= $(LOCAL_LATEX_DIR)/kappak

DOCS_OUTPUT_DIR		= out/docs
DOCS_SRC_DIR		= docs

all: generate docs

check:
	black -l 79 src/*.py
	mypy src/*.py
	pylint src/*.py

clean:
	rm $(LOCAL_KAPPAK_DIR)/*.sty

.PHONY: docs
docs:
	cd $(DOCS_SRC_DIR) && mkdocs build -c -d ../$(DOCS_OUTPUT_DIR)/

generate:
	cd src/ && python3 generate.py

install: uninstall
	mkdir -p $(USER_LATEX_DIR) &&	\
		ln -s "$(realpath $(LOCAL_KAPPAK_DIR))" $(USER_KAPPAK_DIR)

uninstall:
	-rm -rf $(USER_KAPPAK_DIR)
