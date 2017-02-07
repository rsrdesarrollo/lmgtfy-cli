# lmgtfy-cli
Let me Google that for you CLI link generator

## Install

```
python setup.py install
```

## Usage
```
usage: lmgtfy [-h] [-e ENGINE] [--no-clip] query [query ...]

positional arguments:
  query

optional arguments:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        Search engine. valids are web,images,videos,maps,news,
                        shopping,books,finance,schollar. Default:web
  --no-clip             Don't copy url to the clipboard
```

## Samples

Print link to search for Python3 programming books and copy it to the clipboard
```
lmgtfy -e books python3 programming 
```

Print link to search for Python3 programming books but don't copy it to the clipboard
```
lmgtfy -e books --no-clip python3 programming 
```
