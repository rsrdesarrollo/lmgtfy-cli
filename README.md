# lmgtfy-cli
Let me Google that for you CLI link generator

## Install

```
python setup.py install
```

## Usage
```
usage: lmgtfy [-h] [-e ENGINE] query [query ...]

positional arguments:
  query

optional arguments:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        Search engine. valids are web,images,videos,maps,news,
                        shopping,books,finance,schollar. Default:web
```

## Samples

Print link to search for Python3 programming books
```
lmgtfy -e books python3 programming 
```


Copy to clipboard link to search for Python3 programming books
```
lmgtfy -e books python3 programming | xclip -selection c
```
