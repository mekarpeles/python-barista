#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
     ____   __   ____  __  ____  ____  __
    (  _ \ / _\ (  _ \(  )/ ___)(_  _)/ _\
     ) _ (/    \ )   / )( \___ \  )( /    \
    (____/\_/\_/(__\_)(__)(____/ (__)\_/\_/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Barista helps you manage the Flask

    :copyright: (c) 2015 by Mek Karpeles
    :license: see LICENSE for more details.
"""

__title__ = 'barista'
__version__ = '0.0.24'
__author__ = [
    "Mek <michael.karpeles@gmail.com>"
]

import sys
from .create import setup  # NOQA
from .cli import main


if __name__ == "__main__":
    sys.exit(main())

