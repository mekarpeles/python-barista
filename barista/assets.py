#!/usr/bin/env python3.4
#-*-coding: utf-8 -*-

import datetime

empty = ""

def package(name, version, **kwargs):
    """For package.json"""
    return {
        "name": name,
        "version": kwargs.get('version', ''),
        "description": kwargs.get('desc', ''),
        "main": "js/app.js",
        "scripts": {
            "test": "test"
            },
        "repository": {
            "type": "git",
            "url": kwargs.get('repo', '')
            },
        "author": kwargs.get('author', ''),
        "license": kwargs.get('license', ''),
        "devDependencies": {
            }
        }

def header(name, desc="", year="", author="Anonymous", license="BSD", python='3.4'):
    """Header for .py files"""
    year = year or datetime.date.today().year
    return """#!/usr/bin/env python%s
#-*-coding: utf-8 -*-

\"\"\"
    %s
    %s
    %s

    :copyright: (c) %s by %s
    :license: %s, see LICENSE for more details.
\"\"\"

""" % (python, name, "~" * len(name), desc, year, author, license)

config = """import os
import sys
import types
import configparser

path = os.path.dirname(os.path.realpath(__file__))
approot = os.path.abspath(os.path.join(path, os.pardir))

def getdef(self, section, option, default_value):
    try:
        return self.get(section, option)
    except:
        return default_value

config = configparser.ConfigParser()
config.read('%s/settings.cfg' % path)
config.getdef = types.MethodType(getdef, config)

HOST = config.getdef("server", "host", '0.0.0.0')
PORT = int(config.getdef("server", "port", 8080))
DEBUG = bool(int(config.getdef("server", "debug", 1)))
options = {'debug': DEBUG, 'host': HOST, 'port': PORT}
"""

settings = """[server]
host = 0.0.0.0
port = 8080
debug = 1

"""

app = """from flask import Flask
from flask.ext.routing import router
import views
from configs import options

urls = ('/partials/<path:partial>', views.Partial,
        '/<path:uri>', views.Base,
        '/', views.Base
        )
app = router(Flask(__name__), urls)

if __name__ == "__main__":
    app.run(**options)

"""

views = """from flask import render_template
from flask.views import MethodView

class Base(MethodView):
    def get(self, uri=None):
        return render_template('base.html')

class Partial(MethodView):
    def get(self, partial):
        return render_template('partials/%s.html' % partial)

"""

def base(title, static):
    return """
<!doctype html>
<html class="no-js" lang="">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>%s</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script type="text/javascript" src="/%s/build/js/app.js"></script>
        <link rel="stylesheet" type="text/css" href="/%s/build/css/style.css"/>
    </head>
    <body>
        <!--[if lt IE 8]>
            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
	<h1>It works!</h1>

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X','auto');ga('send','pageview');
        </script>
    </body>
</html>
""" % (title, static, static)
