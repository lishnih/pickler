#!/usr/bin/env python
# coding=utf-8

import sys, os
from setuptools import setup

py_version = sys.version_info[:2]
PY3 = py_version[0] == 3
if PY3:
    if py_version < (3, 3):
        raise RuntimeError('On Python 3, Index requires Python 3.3 or better')
else:
    if py_version < (2, 6):
        raise RuntimeError('On Python 2, Index requires Python 2.6 or better')

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    ]

from pickler.lib.info import __version__

if __name__ == '__main__':
    setup(
        name = 'pickler',
        version = __version__,
        author = 'Stan',
        author_email = 'lishnih@gmail.com',
        url = 'http://github.com/lishnih/pickler',
        packages = ['pickler', 'pickler/lib'],
#         scripts = [
#             'scripts/run_pickler.py',
#         ],
        package_data = dict(settings=[]),
        description = 'Pickle Viewer',
        long_description = __doc__,
        platforms = 'any',
        license = 'Public Domain',
        keywords = ['Pickle', 'Viewer', 'Tk'],
        install_requires = install_requires,
        classifiers = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: Public Domain',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Topic :: Utilities',
        ],
    )