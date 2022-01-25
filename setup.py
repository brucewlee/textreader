from setuptools import setup, find_packages

VERSION = '1.1.2'
DESCRIPTION = 'TextReader'
LONG_DESCRIPTION = 'TextReader'

from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'textreader',

  #required for multi-level directory packages
  packages=find_packages(),

  version = '1.1.5',
  license='cc-by-nc-sa-4.0',
  description = 'Many Readability Formulas for General Uses', 
  author = 'Bruce W. Lee',        
  author_email = 'phys.w.s.lee@gmail.com', 
  url = 'https://github.com/brucewlee',
  keywords = ['NLP', 'LINGUISTIC FEATURE', 'READABILITY'], 
  install_requires=[            # I get to this in a second
          'spacy >= 3.0.0, <3.1.0',
          'supar',
          'pandas',
          'nltk',
          'wget'
      ],

  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  include_package_data=True,
)
