.PHONY: clean

NAME 	   	:= HomeWork 2
VERSION		:= 1.0
DEVELOPER 	:= Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPERS)

run: ## Ejecuta la tarea :)
	python main.py

info: ## Muestra la descripcion de la tarea
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Muestra la version de la tarea
	@echo "$(NAME) v$(VERSION)"

install: ## Instala las dependencias de la tarea
	pip install pil
	pip install numpy
	pip install matplotlib
	pip install scikit-image
	pip install opencv-python

clean: ## Elimina archivos temporalmente
	rm -rf utils/__pycache__/
	rm -rf edge_detection/__pycache__/

help: ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
