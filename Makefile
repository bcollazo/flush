build:
	python setup.py sdist

publish:
	twine upload --repository-url "https://test.pypi.org/legacy/" dist/*

publish-prod:
	twine upload dist/*
