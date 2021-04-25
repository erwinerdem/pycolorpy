# pycolorpy

Adds typographical emphasis and text / background color for strings in python.

## Usage

```python
from pycolorpy import black, red, green, yellow, blue, magenta, cyan, white

example_string = red('Hello ', background='magenta') + green('World') + blue('!', options=['blink'])
print(example_string)
```

## Available options

* bright / bold
* dark
* italic
* underline
* blink
* selected

## Available background color

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white
