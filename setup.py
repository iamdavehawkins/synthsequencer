#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='synthsequencer',
      version='0.1',
      description='Python library for playing MIDI instruments',
      author='David Hawkins',
      author_email='iamdavehawkins@gmail.com',
      packages=find_packages(),
      install_requires=['mido', 'python-rtmidi']
     )
