dev-init
========

Automated development environment initialization

Requirements
------------

- Python 3

Usage
-----

```
usage: dev-init.py [-h] [-l] [-n env | -r env | -s env] [environment]

Automated development environment initialization

optional arguments:
  -h, --help            show this help message and exit
  -n env, --new env     define a new environment type
  -r env, --remove env  remove an environment type from the configuration file
  -s env, --show env    show the commands performed for a specific environemnt

  -l, --list            list all the available environment types

  environment           initialize the specified environment in current
                        directory
```
