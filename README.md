# pycolorpy

A tool to easily color text and background in strings using python.

## Usage

```python
from pycolorpy import (black, red, green, yellow, blue, magenta, cyan, white)

example_string = red('Hello ') + green('World') + blue('!', options=['blink'])
print(example_string)
```

## Available options

* bright / bold
* dark
* italic
* underline
* blink
* selected

### **TODO**

* Make background not a bool but a color option.
