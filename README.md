# Modified Goldman code
Here we have a modified Goldman code (as retrieved from the official Allanino GitHub, https://github.com/allanino/DNA) to encode/decode different types of digital data into DNA, generating fragments of 92 bases instead of 117, due to our DNA oligonucleotide synthesis constraints. 
In our github, we provide you the Python script considering this modification together with updating it from python2 version to python3. 
(attach the document to explian the code???)

# Instructions
The first step is to install file2dna using pip:

$ sudo pip install file2dna

Next, you need to replace the dna.py generated in the folder with our current modified and updated dna.py. Next you can use the following arguments, based on what do you want to achieve:

$ dna -h

usage: dna [-h] [-e | -s | -d | -j] file

positional arguments:

  file        File to be encoded/decoded.

optional arguments:

  -h, --help  show this help message and exit
  
  -e          encode file and save it as .dna
  
  -s          encode file and save it as .splitted.zip
  
  -d          decode .dna file and save as .decoded
  
  -j          decode .splitted.zip file and save it as .decoded

In our textaDNA project, we have used this code first to encode and retrieve a short quote and the logo of our research center, in silico, and next to scale up to try in vitro experiments with real data and real DNA sequences. You can see the used files as examples in this repository. 
  
