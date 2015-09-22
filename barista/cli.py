#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    cli.py
    ~~~~~~

    The command line interface for Barista

    :copyright: (c) 2015 by Mek Karpeles
    :license: see LICENSE for more details.
"""

import os
import sys
import argparse
import pypc
from .create import setup


def argparser():
    parser = argparse.ArgumentParser(
        description="Barista helps you with your Flask.")
    parser.add_argument('name', nargs='?', metavar='name', default='app',
                        help="Create a new Flask web application")
    parser.add_argument('--pkg', dest='pkg', default=None,
                        help='Create a package')
    return parser


def main():
    parser = argparser()
    args = parser.parse_args()
    path = os.path.abspath(os.getcwd())

    if not args.name:
        sys.exit(parser.print_help())

    if args.pkg:
        # pypc.create.Package(args.name, path=path)
        # path = os.path.join(path, os.sep, args.name)
        pass

    setup(path, appname=args.name)
