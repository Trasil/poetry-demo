# [Poetry](https://python-poetry.org/) demo

Poetry - инструмент для управления зависимостями в Python проектах (аналог встроенного pip).

## Install

``` bash
pip install poetry
```

## Instal dependencies
``` bash
# для первичной установки
poetry install
# для обновления
poetry update
```

## Run project
``` bash
poetry run demo
```

### Usage:
``` txt
usage: demo [-h] [--random {int,real}] [--output OUTPUT] [a] [b] [n] [k]

Dynamic histogram work demo

positional arguments:
  a                     The left boundary of the uniform distribution of a random variable
  b                     The right boundary of the uniform distribution of a random variable
  n                     Number of histogram intervals
  k                     The number of points per one interval of the dynamic histogram

options:
  -h, --help            show this help message and exit
  --random {int,real}, -r {int,real}
                        Set type of random variable: integer(int) or real(real)
  --output OUTPUT, -o OUTPUT
                        The name of the file in which information about the difference between normal and dynamic histograms will be placed
```

## Run checks
### Tests
``` bash
poetry run pytest
```

### Check stryle
``` bash
poetry run black --check ./trasil
poetry run isort --check ./trasil
```

## Install
### Build
``` bash
# Create package
poetry build

# Install
pip install dist/poetry_demo-<version>-py3-none-any.whl
```
### Use
#### Run in terminal
``` bash
demo
```

#### Use in python project
``` python
from trasil.dynamichistogram import ClassicHistogram
```
