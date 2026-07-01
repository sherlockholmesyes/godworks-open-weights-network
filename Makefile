.PHONY: demo test

demo:
	python -m gown_poc.demo

test:
	python -m unittest discover -s tests
