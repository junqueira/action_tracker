help:
	@echo "setup        install production packages"
	@echo "dev          install development packages"
	@echo "test         run default test suit"
	@echo "clean        remove all trash files"

setup:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

test:
	python setup.py test

clean:
	find . -name "*.pyc" -delete
	rm -rf build
	rm -rf dist
	rm README.rst
