import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='txotxdna',
    version='none',
    author='textadna',
    author_email='textadna.eu',
    description='Encode/decode digital files into DNA sequences.',
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
