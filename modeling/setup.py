
# pip install -e or python setup.py develop to modularize pacakges in editable setting



from setuptools import setup, find_packages

setup(
		name = 'breast_cancer_project',
		version = '1.0',
		packages = find_packages()
	)