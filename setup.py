from setuptools import setup
from setuptools import find_packages

REQUIRED_PYTHON = (3, 1)

setup(name='RDriver',
      version='0.1.0',
      python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
      description='Streamlining Selenium for web scraping',
      long_description=open('README.md').read(),
      url='https://github.com/jcomish/RDriver',
      author='Joshua Comish',
      author_email='jcomish@sourceiron.com',
      license='Apache 2.0',
      keywords='automation web scraping selenium',
      # packages=['RDriver.py'],
      py_modules=["RDriver"],
      install_requires=['selenium>=3.12.0'],
      tests_require=['pytest'])