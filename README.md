# pycolorpy

[![PyPi](https://img.shields.io/pypi/v/pycolorpy?logo=PyPI)](https://pypi.org/project/pycolorpy)
[![PyPI license](https://img.shields.io/pypi/l/pycolorpy.svg)](https://pypi.python.org/pypi/pycolorpy/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/pycolorpy.svg)](https://pypi.python.org/pypi/pycolorpy/)
[![PyPI format](https://img.shields.io/pypi/format/pycolorpy.svg)](https://pypi.python.org/pypi/pycolorpy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Adds typographical emphasis and text / background color for strings in python.

## Installation

```bash
pip install pycolorpy
```

## Usage

```python
from pycolorpy import black, red, green, yellow, blue, magenta, cyan, white

example_string = yellow('Hello ', options=['blink'], background='red') + magenta('World', options=['underline', 'italic'], background='green') + cyan('!')
print(example_string)
```

## Available options

* bright
* dark
* italic
* underline
* blink
* selected

## Available background colors

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white
