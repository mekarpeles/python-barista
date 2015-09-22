#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
    create.py
    ~~~~~~~~~

    Barista helps you manage the Flask

    :copyright: (c) 2015 by Mek Karpeles
    :license: see LICENSE for more details.
"""

import os
import json
import datetime
import textwrap
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('barista', 'templates'))


def setup(path, appname="app", version="0.0.1", python='3.4', **kwargs):
    static = kwargs.pop('static', 'static')
    fs = {
        '%s.py' % appname: env.get_template('app.py').render(),
        'uwsgi.ini': env.get_template('uwsgi.ini').render(
            path=path, appname=appname, python='3.4'),
        static: {
            'styles': {},
            'scripts': {},
            'images': {}
        },
        kwargs.pop('frontend', 'frontend'): {
            'styles': {
                'style.scss': ''
            },
            'scripts': {
                'main.js': ''
            }
        },
        kwargs.pop('templates', 'templates'): {
            'base.html': env.get_template('base.html').render(
                appname=appname),
            'partials': {
                'index.html': '<h1>It works!</h1>'
            }
        },
        kwargs.pop('views', 'views'): {
            '__init__.py': env.get_template('views.py').render(),
            'endpoints.py': env.get_template('endpoints.py').render(),
        },
        kwargs.pop('configs', 'configs'): {
            '__init__.py': env.get_template('config.py').render(),
            'settings.cfg': env.get_template('settings.cfg').render()
        },
        kwargs.pop('tests', 'tests'): {
            '__init__.py': ""
        }
    }
    buildfs(fs, path=path, **kwargs)


def header(name, year="", author="Anonymous", python='3.4', encoding="utf-8"):
    """Header for .py files"""
    year = year or datetime.date.today().year
    underline = len(name) * '~'
    #desc = textwrap.fill(desc, width=79)
    return env.get_template('header.html').render(
        encoding=encoding, name=name, underline=underline,
        year=year, author=author
        )


def buildfs(fs, path="", **kwargs):
    if type(fs) is not dict:
        return create_asset(fs, path, **kwargs)

    for f in fs:
        cwd = "%s%s%s" % (path, os.sep, f)
        if type(fs[f]) is dict:
            if not os.path.exists(cwd):
                os.makedirs(cwd)
            buildfs(fs[f], path=cwd, **kwargs)
        else:
            create_asset(fs[f], cwd)


def create_asset(asset, path, **kwargs):
    if asset and not os.path.exists(path):
        fname = path.rsplit(os.sep, 1)[-1]
        if fname.endswith(".py"):
            python = kwargs.get('python', '')
            asset = header(fname, python=python) + asset
        with open(path, 'w') as fout:
            fout.write(asset)
