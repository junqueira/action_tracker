help:
	@echo "setup        install production packages"
	@echo "build        create packages"
	@echo "register     register package on PyPI"
	@echo "dev          install development packages"
	@echo "test         run default test suit"
	@echo "clean        remove all trash files"

setup:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

build:
	python setup.py sdist build

register: build
	python setup.py register

test:
	python setup.py test

clean:
	find . -name "*.pyc" -delete
	rm -rf build
	rm -rf dist
