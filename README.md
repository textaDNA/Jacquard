# Modified Goldman code
Here we have a modified Goldman code (as retrieved from the official Allanino GitHub, https://github.com/allanino/DNA) to encode/decode different types of digital data into DNA, generating fragments of 92 bases instead of 117, due to our DNA oligonucleotide synthesis constraints. 
In our github, we provide you the Python script considering this modification. The program runs on Python3. 
For more information on how the code itself operates, you can read the original Goldman et al., article (https://www.nature.com/articles/nature11875). 

# Instructions
The first step is to install file2dna using pip:

```python
$ sudo pip install file2dna
```

Next, you need to replace the dna.py saved in the folder created with our current modified and updated dna.py. You can then use the following arguments directly on the terminal, based on what do you want to achieve:

```python
$ dna -... file

usage: dna [-h] [-e | -s | -d | -j] file

positional arguments:

  file        "It is the file to be encoded/decoded."

optional arguments:

  -h, --help  show this help message and exit
  
  -e          encodes file, saves it ".dna"
  
  -s          encodes file, saves it ".splitted.zip"
  
  -d          decodes ".dna" file, saves it ".decoded"
  
  -j          decodes ".splitted.zip" file, saves it ".decoded"
```
In our textaDNA project, we have used this code first to encode and retrieve a short quote and the logo of our research center, <i>in silico</i>, and next to scale up to try <i>in vitro</i> experiments with real data and real DNA sequences. You can see the used files as examples in this repository. 
  
