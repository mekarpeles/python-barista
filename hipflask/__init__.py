#!/usr/bin/env python3.4
#-*-coding: utf-8 -*-

"""
    __init__
    ~~~~~~~~
    Setup flapper app with

    :copyright: (c) 2015 by Mek
    :license: BSD, see LICENSE for more details.
"""

import os
from . import assets

def setup(path, appname="app.py", version="0.0.1", python='3.4', **kwargs):
    static = kwargs.pop('static', 'static')
    fs = {
        'app.py': assets.app,
        static: {
            'package.json': assets.package(appname, version),
            'Gulpfile.js': assets.empty,
            'build': {
                'css': {},
                'imgs': {},
                'js': {},
                'fonts': {}
                },
            'styles': {'style.less': assets.empty},
            'js': {'app.js': assets.empty},
            'fonts': {},
            'imgs': {}
            },
        kwargs.pop('templates', 'templates'): {
            'base.html': assets.base(appname, static),
            'partials': {}
            },
        kwargs.pop('views', 'views'): {
            '__init__.py': assets.views
            },
        kwargs.pop('configs', 'configs'): {
            '__init__.py': assets.config,
            'settings.cfg': assets.settings
            },
        kwargs.pop('tests', 'tests'): {
            '__init__.py': assets.empty
            },
        }

    def buildfs(fs, path=""):
        def buildfile(asset, path):
            if asset and not os.path.exists(path):
                if f.endswith(".py"):
                    asset = assets.header(f, python=python) + asset
                with open(path, 'w') as fout:
                    fout.write(asset)

        if type(fs) is not dict:
            buildfile(fs, path)
        else:
            for f in fs:
                cwd = "%s%s%s" % (path, os.sep, f)
                # if f is a directory
                if type(fs[f]) is dict:
                    if not os.path.exists(cwd):
                        os.makedirs(cwd)
                    if fs[f]: # non empty dir
                        buildfs(fs[f], path=cwd)
                else:
                    buildfile(fs[f], path=cwd)

    buildfs(fs, path=path)
