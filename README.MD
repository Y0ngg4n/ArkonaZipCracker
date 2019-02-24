# ArkonaZipCracker

Arkona is a small and lightweight free to use ZIP and RAR Cracker based on Python.

It contains following features:

  - Generating a Password-List based on a Regex-Expression
  - Using a password List with the Option to start at a custom offset
  - Bruteforcing all Passwords based on a Regex-Expression

### Installation

Arkona requires:
  - [rarfile](https://pypi.org/project/rarfile/)
  - [zipfile](https://docs.python.org/3/library/zipfile.html)
  - [exrex](https://github.com/asciimoo/exrex)

Install the dependencies with this command:

```sh
$ pip install rarfile zipfile exrex
```

### How to use

To use Arkona you just have to execute the Python file:

```sh
$ python cracker.py
```