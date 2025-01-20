# Jacquard: modified Goldman algorithm for DNA data storage

Jacquard is a Python tool for encoding files into DNA sequences and decoding them back. It is a modified Goldman algorithm [[1]](https://www.nature.com/articles/nature11875) and adapted from the [DNA script](https://github.com/allanino/DNA).

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [References](#references)
- [License](#license)

## Introduction

This repository provides a modified version of the Goldman code to encode and decode various types of digital data into DNA sequences. The program runs on Python 3.For more information on the original Goldman code, please refer to [[1]](https://www.nature.com/articles/nature11875).

## Installation

To install Jacquard, use the following command:

```sh
pip install git+https://github.com/textaDNA/Jacquard.git
```

Alternatively, you can install Jacquard using `setup.py` with the following command:

```sh
python setup.py install
```

## Usage

Once installed, you can use the following commands in the terminal based on what you want to achieve:

```sh
dna [option] file
```

### Positional Arguments

- `-h, --help`: Show the help message and exit.
- `-e`: Encode the file and save it as `.dna`.
- `-s`: Encode the file and save it as `.splitted.zip`.
- `-d`: Decode the `.dna` file and save it as `.decoded`.
- `-j`: Decode the `.splitted.zip` file and save it as `.decoded`.

### Example Commands

To encode a file "quote":

```sh
dna -e /path/to/quote.txt
```

The resulting DNA string will be saved in the same directory. To decode it:

```sh
dna -d /path/to/quote.txt.dna
```

Ensure you provide the correct file extension according to the command you want to use.

## Examples

In the textaDNA project, we have used this code to encode a short quote and the logo of the research center CiC Naogune. The resulting sequenced files are then used to decode the files back. 

## References

- [1. Goldman algorithm ](https://www.nature.com/articles/nature11875)
- [2. DNA script](https://github.com/allanino/DNA)
- [3. TextaDNA project](https://textadna.eu)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
