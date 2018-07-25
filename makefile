DIRECTORY=~/texmf/tex/latex
TARGET=$(DIRECTORY)/kappak

autocompletion:
	@python3 generate.py
	@echo "Autocompletion fles generated. Please refer to README.md for installation instructions."

install:
	@mkdir -p $(DIRECTORY)
	@[ -d $(TARGET) ] || ln -s "$(realpath src)" $(TARGET)

uninstall:
	@rm $(TARGET)