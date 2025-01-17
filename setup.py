import os
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='file2dna',
    version='0.4',
    author='textadna',
    author_email='textadna.eu',
    description='A script to encode/decode arbitrary computer files into DNA sequences.',
    url='https://github.com/textaDNA/Jacquard',
    packages=['dna'],
    include_package_data=True,
    license='MIT',
    keywords='dna encoding decoding file',
    long_description=read('README.md'),
    entry_points={
        'console_scripts': ['dna=dna.dna:main'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
