dev-init
========

[![PyPI version](https://img.shields.io/pypi/v/dev-init.svg)](https://pypi.python.org/pypi/dev-init)

Automated development environment initialization

Requirements
------------

- Python 2 or 3 (tested in Python 2.7 and 3.4)

Usage
-----

```
usage: dev_init [-h] [--version] [-l] [-n | -r | -s] [environment]

Automated development environment initialization

positional arguments:
  environment   initialize the specified environment in current directory

optional arguments:
  -h, --help    show this help message and exit
  --version     show program's version number and exit
  -l, --list    list all the available environment types
  -n, --new     define a new environment type
  -r, --remove  remove an environment type from the configuration file
  -s, --show    show the commands performed for a specific environemnt
```
