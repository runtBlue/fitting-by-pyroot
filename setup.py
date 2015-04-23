#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
  name             = 'fitting-root-exmerimentally',
  version          = '0.0.1',
  description      = 'fitting by ROOT',
  license          = 'MIT',
  author           = 'Hiroki Takagishi',
  author_email     = 'a@b.c',
  url              = 'https://github.com/runtBlue/fitting-by-pyroot',
  keywords         = 'ROOT PyROOT Fitting Math',
  packages         = find_packages(),
  install_requires = [
    'setuptools',
    'numpy',
  ],
)