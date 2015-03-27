#!/usr/bin/env python3.4
#-*-coding: utf-8 -*-

import json
import datetime

def package(name, version, **kwargs):
    """For package.json"""
    return json.dumps({
        "name": name,
        "version": kwargs.get('version', ''),
        "description": kwargs.get('desc', ''),
        "main": "build/js/" + name + ".js",
        "scripts": {
            "test": "test"
        },
        "repository": {
            "type": "git",
            "url": kwargs.get('repo', '')
        },
        "author": kwargs.get('author', ''),
        "license": kwargs.get('license', ''),
        "dependencies": {
            "angular": "^1.3.15",
            "angular-ui-router": "^0.2.13",
            "angular-mocks": "^1.3.15",
            "brfs": "^1.4.0",
            "browser-sync": "^1.9.1",
            "browserify-ngannotate": "^0.1.0",
            "express": "^4.12.3",
            "gulp": "^3.8.11",
            "gulp-angular-templatecache": "^1.5.0",
            "del": "^0.1.3",
            "browserify": "^5.13.1",
            "gulp-changed": "^1.2.1",
            "browserify-shim": "^3.8.3",
            "gulp-imagemin": "^1.2.1",
            "gulp-if": "^1.2.5",
            "gulp-karma": "^0.0.4",
            "gulp-notify": "^2.2.0",
            "gulp-protractor": "^0.0.11",
            "gulp-rename": "^1.2.0",
            "gulp-jshint": "^1.9.4",
            "gulp-streamify": "^0.0.5",
            "gulp-autoprefixer": "^2.1.0",
            "gulp-util": "^3.0.4",
            "gulp-uglify": "^1.1.0",
            "gulp-sass": "^0.7.3",
            "karma": "^0.12.31",
            "karma-chrome-launcher": "^0.1.7",
            "jshint-stylish": "^1.0.1",
            "karma-firefox-launcher": "^0.1.4",
            "karma-jasmine": "^0.1.5",
            "morgan": "^1.5.2",
            "pretty-hrtime": "^0.2.2",
            "protractor": "^1.8.0",
            "run-sequence": "^0.3.7",
            "tiny-lr": "^0.0.9",
            "uglifyify": "^2.6.0",
            "vinyl-source-stream": "^0.1.1",
            "watchify": "^2.5.0",
            "imagemin-pngcrush": "^0.1.0",
            "karma-bro": "^0.7.1"
        },
        "devDependencies": {}
    })

def bower_json(name, version, **kwargs):
    """For bower.json"""
    return json.dumps({
        "name": name,
        "version": kwargs.get('version', ''),
        "homepage": kwargs.get('repo', ''),
        "authors": [
            kwargs.get('author', '')
        ],
        "description": kwargs.get('desc', ''),
        "main": "build/css/" + name + ".css",
        "keywords": [],
        "license": kwargs.get('license', ''),
        "ignore": [
            "**/.*",
            "node_modules",
            "bower_components",
            "test",
            "tests"
        ],
        "dependencies": {
            "fever": "*"
        }
    })

def header(name, desc="", year="", author="Anonymous", license="", python='3.4'):
    """Header for .py files"""
    year = year or datetime.date.today().year
    license = " %s," % license if license else ""
    return """#!/usr/bin/env python%s
#-*-coding: utf-8 -*-

\"\"\"
    %s
    %s
    %s

    :copyright: (c) %s by %s
    :license:%s see LICENSE for more details.
\"\"\"

""" % (python, name, "~" * len(name), desc, year, author, license)

config = """import os
import sys
import types
try:
    import ConfigParser as configparser
except:
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
template_folder = 'static/app/views'
options = {
    'debug': DEBUG,
    'host': HOST,
    'port': PORT,
}
"""

settings = """[server]
host = 0.0.0.0
port = 8080
debug = 1

"""

app = """from flask import Flask
from flask.ext.routing import router
import views
from configs import options, template_folder

urls = ('/partials/<path:partial>', views.Partial,
        '/<path:uri>', views.Base,
        '/', views.Base
        )
app = router(Flask(__name__, template_folder=template_folder), urls)

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

def base(appname, static):
    return """<!doctype html>
<html class="no-js" lang="">
  <head>
    <base href="/">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title ng-bind="pageTitle"></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script type="text/javascript" src="/static/build/js/%(appname)s.js"></script>
    <link rel="stylesheet" type="text/css" href="/static/build/css/%(appname)s.css"/>
  </head>
  <body>
    <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

    <div ui:view></div>

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
""" %{'appname': appname}

gulpfile = """'use strict';

/*
 * Gulpfile.js
 * ===========
 * Rather than manage one giant configuration file responsible
 * for creating multiple tasks, each task has been broken out into
 * its own file in gulp/tasks. Any file in that folder gets automatically
 * required by the loop in ./gulp/index.js (required below).
 *
 * To add a new task, simply add a new task file to gulp/tasks.
 */

global.isProd = false;

require('./gulp');
"""

def gulp_config(appname):
    return """'use strict';

module.exports = {

  'serverport': 3000,

  'styles': {
    'src' : 'app/styles/**/*.scss',
    'dest': 'build/css'
  },

  'scripts': {
    'src' : 'app/scripts/**/*.js',
    'dest': 'build/js'
  },

  'images': {
    'src' : 'app/images/**/*',
    'dest': 'build/images'
  },

  'fonts': {
    'src' : 'app/fonts/*',
    'dest': 'build/fonts'
  },

  'views': {
    'watch': [
      'app/index.html',
      'app/views/**/*.html',
      'app/**/views/*.html'
    ],
    'src': 'app/views/**/*.html',
    'dest': 'app/scripts'
  },

  'dist': {
    'root'  : 'build'
  },

  'browserify': {
    'entries'   : ['./app/scripts/%(appname)s.js'],
    'bundleName': '%(appname)s.js'
  },

  'test': {
    'karma': 'test/karma.conf.js',
    'protractor': 'test/protractor.conf.js'
  }

};
""" % {'appname': appname}

gulp_index = """'use strict';

var fs = require('fs');
var onlyScripts = require('./util/scriptFilter');
var tasks = fs.readdirSync('./gulp/tasks/').filter(onlyScripts);

tasks.forEach(function(task) {
  require('./tasks/' + task);
});
"""
    
def gulp_tasks(appname):
    return {
        'browserSync.js': """'use strict';

var config      = require('../config');
var browserSync = require('browser-sync');
var gulp        = require('gulp');

    gulp.task('browserSync', function() {

  browserSync({
    proxy: 'localhost:' + config.serverport
  });

});    
""",
    'browserify.js': """'use strict';

var config       = require('../config');
var gulp         = require('gulp');
var gulpif       = require('gulp-if');
var gutil        = require('gulp-util');
var source       = require('vinyl-source-stream');
var streamify    = require('gulp-streamify');
var watchify     = require('watchify');
var browserify   = require('browserify');
var uglify       = require('gulp-uglify');
var handleErrors = require('../util/handleErrors');
var browserSync  = require('browser-sync');
var ngAnnotate   = require('browserify-ngannotate');

// Based on: http://blog.avisi.nl/2014/04/25/how-to-keep-a-fast-build-with-browserify-and-reactjs/
function buildScript(file) {

  var bundler = browserify({
    entries: config.browserify.entries,
    cache: {},
    packageCache: {},
    fullPaths: true
    }, watchify.args);

  if ( !global.isProd ) {
    bundler = watchify(bundler);
    bundler.on('update', function() {
      rebundle();
    });
  }

  bundler.transform(ngAnnotate);
  bundler.transform('brfs');

  function rebundle() {
    var stream = bundler.bundle();

    gutil.log('Rebundle...');

    return stream.on('error', handleErrors)
      .pipe(source(file))
      .pipe(gulpif(global.isProd, streamify(uglify())))
      .pipe(gulp.dest(config.scripts.dest))
      .pipe(browserSync.reload({ stream: true, once: true }));
  }

  return rebundle();

}

    gulp.task('browserify', function() {

    return buildScript('%(appname)s.js');

});
"""%{'appname': appname},
    'clean.js': """'use strict';

var config = require('../config');
var gulp   = require('gulp');
var del    = require('del');

    gulp.task('clean', function(cb) {

    del([config.dist.root], cb);

});
""",
    'deploy.js': """'use strict';

var gulp = require('gulp');

    gulp.task('deploy', function() {

  // Any deployment logic should go here

});
""",
    'development.js': """'use strict';

var gulp        = require('gulp');
var runSequence = require('run-sequence');

gulp.task('dev', ['clean'], function(cb) {

  cb = cb || function() {};

  global.isProd = false;

    runSequence('styles', 'images', 'fonts', 'views', 'browserify', 'watch', cb);

});
""",
    'fonts.js': """'use strict';

var config     = require('../config');
var changed    = require('gulp-changed');
var gulp       = require('gulp');
var gulpif     = require('gulp-if');

gulp.task('fonts', function() {

  var dest = config.fonts.dest;

  return gulp.src(config.fonts.src)
    .pipe(changed(dest)) // Ignore unchanged files
    .pipe(gulp.dest(dest));

});
""",
    'images.js': """'use strict';

var config     = require('../config');
var changed    = require('gulp-changed');
var gulp       = require('gulp');
var gulpif     = require('gulp-if');
var imagemin   = require('gulp-imagemin');

gulp.task('images', function() {

  var dest = config.images.dest;

  return gulp.src(config.images.src)
    .pipe(changed(dest)) // Ignore unchanged files
    .pipe(gulpif(global.isProd, imagemin()))    // Optimize
    .pipe(gulp.dest(dest));

});
""",
    'lint.js': """'use strict';

var config = require('../config');
var gulp   = require('gulp');
var jshint = require('gulp-jshint');

gulp.task('lint', function() {
    return gulp.src([config.scripts.src, '!app/js/templates.js'])
    .pipe(jshint())
    .pipe(jshint.reporter('jshint-stylish'));
});
""",
    'production.js': """'use strict';

var gulp        = require('gulp');
var runSequence = require('run-sequence');

gulp.task('prod', ['clean'], function(cb) {

  cb = cb || function() {};

  global.isProd = true;

    runSequence('styles', 'images', 'views', 'browserify', cb);

});
""",
    'protractor.js': """'use strict';

var gulp            = require('gulp');
var protractor      = require('gulp-protractor').protractor;
var webdriver       = require('gulp-protractor').webdriver;
var webdriverUpdate = require('gulp-protractor').webdriver_update;
var config          = require('../config');

gulp.task('webdriver-update', webdriverUpdate);
gulp.task('webdriver', webdriver);

gulp.task('protractor', ['webdriver-update', 'webdriver', 'server'], function() {

  return gulp.src('test/e2e/**/*.js')
    .pipe(protractor({
        configFile: config.test.protractor,
    }))
    .on('error', function(err) {
      // Make sure failed tests cause gulp to exit non-zero
      throw err;
    });

});
""",
    'reload.js': """'use strict';

var gulp        = require('gulp');
var browserSync = require('browser-sync');

gulp.task('reload', function() {

  browserSync.reload();

});
""",
    'server.js': """'use strict';

var config  = require('../config');
var http    = require('http');
var express = require('express');
var gulp    = require('gulp');
var gutil   = require('gulp-util');
var morgan  = require('morgan');

gulp.task('server', function() {

  var server = express();

  // log all requests to the console
  server.use(morgan('dev'));
  server.use(express.static(config.dist.root));

  // Serve index.html for all routes to leave routing up to Angular
    server.all('/*', function(req, res) {
      res.sendFile('index.html', { root: 'build' });
  });

  // Start webserver if not already running
  var s = http.createServer(server);
    s.on('error', function(err){
    if(err.code === 'EADDRINUSE'){
      gutil.log('Development server is already started at port ' + config.serverport);
    }
    else {
      throw err;
    }
  });

  s.listen(config.serverport);

});
""",
    'styles.js': """'use strict';

var config       = require('../config');
var gulp         = require('gulp');
var sass         = require('gulp-sass');
var gulpif       = require('gulp-if');
var handleErrors = require('../util/handleErrors');
var browserSync  = require('browser-sync');
var autoprefixer = require('gulp-autoprefixer');

gulp.task('styles', function () {

  return gulp.src(config.styles.src)
    .pipe(sass({
      sourceComments: global.isProd ? 'none' : 'map',
      sourceMap: 'sass',
      outputStyle: global.isProd ? 'compressed' : 'nested'
    }))
    .pipe(autoprefixer("last 2 versions", "> 1%", "ie 8"))
    .on('error', handleErrors)
    .pipe(gulp.dest(config.styles.dest))
    .pipe(gulpif(browserSync.active, browserSync.reload({ stream: true })));

});
""",
    'test.js': """'use strict';

var gulp        = require('gulp');
var runSequence = require('run-sequence');

gulp.task('test', ['server'], function() {

    runSequence('unit', 'protractor');

});
""",
    'unit.js': """'use strict';

var gulp   = require('gulp');
var karma  = require('gulp-karma');
var config = require('../config');

gulp.task('unit', function() {

    // Nonsensical source to fall back to files listed in karma.conf.js,
  // see https://github.com/lazd/gulp-karma/issues/9
  return gulp.src('./thisdoesntexist')
    .pipe(karma({
      configFile: config.test.karma,
      action: 'run'
    }))
    .on('error', function(err) {
      // Make sure failed tests cause gulp to exit non-zero
      throw err;
    });

});
""",
    'views.js': """'use strict';

var config         = require('../config');
var gulp           = require('gulp');
var templateCache  = require('gulp-angular-templatecache');

// Views task
gulp.task('views', function() {

  // Put our index.html in the dist folder
  gulp.src('app/views/base.html')
    .pipe(gulp.dest(config.dist.root));

  // Process any other view files from app/views
  return gulp.src(config.views.src)
    .pipe(templateCache({
      standalone: true
    }))
    .pipe(gulp.dest(config.views.dest));

});
""",
    'watch.js': """'use strict';

var config        = require('../config');
var gulp          = require('gulp');

gulp.task('watch', ['browserSync', 'server'], function() {

    gulp.watch(config.scripts.src, ['lint', 'browserify']);
    gulp.watch(config.styles.src,  ['styles']);
    gulp.watch(config.images.src,  ['images', 'reload']);
    gulp.watch(config.views.watch, ['views']);

});
""",
    'build.js': """'use strict';

var gulp        = require('gulp');
var runSequence = require('run-sequence');

gulp.task('build', ['clean'], function(cb) {

  cb = cb || function() {};

  global.isProd = false;

  runSequence('styles', 'images', 'fonts', 'views', 'browserify', cb);

});
"""
}

def gulp_util(appname):
    return {
        'bundleLogger.js': """'use strict';

/* bundleLogger
 * ------------
 * Provides gulp style logs to the bundle method in browserify.js
 */

var gutil        = require('gulp-util');
var prettyHrtime = require('pretty-hrtime');
var startTime;

module.exports = {

  start: function() {
    startTime = process.hrtime();
        gutil.log('Running', gutil.colors.green('\'bundle\'') + '...');
        },

  end: function() {
    var taskTime = process.hrtime(startTime);
    var prettyTime = prettyHrtime(taskTime);
        gutil.log('Finished', gutil.colors.green('\'bundle\''), 'in', gutil.colors.magenta(prettyTime));
  }

};
""",
        'handleErrors.js': """'use strict';

var notify = require('gulp-notify');

module.exports = function(error) {

  if( !global.isProd ) {

    var args = Array.prototype.slice.call(arguments);

    // Send error to notification center with gulp-notify
    notify.onError({
        title: 'Compile Error',
      message: '<%= error.message %>'
        }).apply(this, args);

    // Keep gulp from hanging on this task
    this.emit('end');

  } else {
    // Log the error and stop the process
    // to prevent broken code from building
    console.log(error);
    process.exit(1);
  }

};
""",
        'scriptFilter.js': """'use strict';

var path = require('path');

// Filters out non .js files. Prevents
// accidental inclusion of possible hidden files
module.exports = function(name) {

  return /(\.(js)$)/i.test(path.extname(name));

};
"""
}

def test_e2e():
    return {
        'example_spec.js': """/*global browser, by */

'use strict';

        describe('E2E: Example', function() {

  beforeEach(function() {
    browser.get('/');
    browser.waitForAngular();
  });

        it('should route correctly', function() {
    expect(browser.getLocationAbsUrl()).toMatch('/');
  });

        it('should show the number defined in the controller', function() {
    var element = browser.findElement(by.css('.number-example'));
    expect(element.getText()).toEqual('1234');
  });

});
""",
        'routes_spec.js': """/*global browser */

'use strict';

        describe('E2E: Routes', function() {

        it('should have a working home route', function() {
    browser.get('#/');
    expect(browser.getLocationAbsUrl()).toMatch('/');
  });

});
"""
}

def test_unit_controllers():
    return {
        'example_spec.js': """/*global angular */

'use strict';

        describe('Unit: ExampleCtrl', function() {

  var ctrl;

  beforeEach(function() {
    // instantiate the app module
    angular.mock.module('app');

    // mock the controller
    angular.mock.inject(function($controller) {
      ctrl = $controller('ExampleCtrl');
    });
  });

        it('should exist', function() {
    expect(ctrl).toBeDefined();
  });

        it('should have a number variable equal to 1234', function() {
    expect(ctrl.number).toEqual(1234);
  });

        it('should have a title variable equal to \'AngularJS, Gulp, and Browserify!\'', function() {
        expect(ctrl.title).toEqual('AngularJS, Gulp, and Browserify!');
  });

});
"""
}

def test_unit_services():
    return {
        'example_spec.js': """/*global angular */

'use strict';

        describe('Unit: ExampleService', function() {

  var service;

  beforeEach(function() {
    // instantiate the app module
    angular.mock.module('app');

    // mock the service
    angular.mock.inject(function(ExampleService) {
      service = ExampleService;
    });
  });

        it('should exist', function() {
    expect(service).toBeDefined();
  });

});
"""
}

test_unit_settings_spec = """/*global angular */

'use strict';

describe('Unit: Settings', function() {

  var settings;

  beforeEach(function() {
    // instantiate the app module
    angular.mock.module('app');

    // mock the directive
    angular.mock.inject(function(AppSettings) {
      settings = AppSettings;
    });
  });

  it('should exist', function() {
    expect(settings).toBeDefined();
  });

  it('should have an application name', function() {
    expect(settings.appTitle).toEqual('Example Application');
  });

});
"""

def test_karma(appname):
    return """'use strict';

module.exports = function(config) {

  config.set({

    basePath: '../',
    frameworks: ['jasmine', 'browserify'],
    preprocessors: {
      'app/scripts/**/*.js': ['browserify']
    },
    browsers: ['Chrome'],
    reporters: ['progress'],

    autoWatch: true,

    plugins: [
      'karma-jasmine',
      'karma-bro',
      'karma-chrome-launcher',
      'karma-firefox-launcher'
    ],

    proxies: {
      '/': 'http://localhost:9876/'
    },

    urlRoot: '/__karma__/',

    files: [
      // 3rd-party resources
      'node_modules/angular-mocks/angular-mocks.js',

      // app-specific code
      'app/scripts/%(appname)s.js',

      // test files
      'test/unit/**/*.js'
    ]

  });

};
""" % {'appname': appname}

test_protractor = """'use strict';

exports.config = {

  allScriptsTimeout: 11000,

  baseUrl: 'http://localhost:3000/',

  capabilities: {
    browserName: 'chrome',
    version: '',
    platform: 'ANY'
  },

  framework: 'jasmine',

  jasmineNodeOpts: {
    isVerbose: false,
    showColors: true,
    includeStackTrace: true,
    defaultTimeoutInterval: 30000
  },

  specs: [
    'e2e/**/*.js'
  ]

};
"""

class Angular(object):

    @staticmethod
    def config(appname):
        return """'use strict';

var AppSettings = {
  appTitle: '%(appname)s',
  apiPath: '/api/v1'
};

module.exports = AppSettings;
""" % {'appname': appname}
    
    @staticmethod
    def directives(appname):
        return """
'use strict';

var angular = require('angular');

module.exports = angular.module('%(appname)s.directives', []);

// Define the list of directives here
//require('./example.js');
""" % {'appname': appname}

    @staticmethod
    def services(appname):
        return """'use strict';

var angular = require('angular');

module.exports = angular.module('%(appname)s.services', []);

// Define the list of services here
// require('./user.js');
""" % {'appname': appname}

    @staticmethod
    def controllers(appname):
        return {
            '_index.js': """'use strict';    

var angular = require('angular');

module.exports = angular.module('%(appname)s.controllers', []);

// Define the list of controllers here
require('./landing.js');
""" % {'appname': appname},
            'landing.js': """'use strict';

var %(appname)sControllers = require('./_index');

/**
 * @ngInject
 */

function LandingCtrl($stateParams, $timeout) {

  // ViewModel
  var landing = this;

  landing.title = "home";

}

%(appname)sControllers.controller('LandingCtrl', LandingCtrl);
""" % {'appname': appname}
        }

    @staticmethod
    def app(appname):
        return """'use strict';

var angular = require('angular');

// angular modules
require('angular-ui-router');
require('./templates');
require('./controllers/_index');
require('./services/_index');
require('./directives/_index');

// create and bootstrap application
angular.element(document).ready(function() {

  var requires = [
    'ui.router',
    '%(appname)s.controllers',
    '%(appname)s.services',
    '%(appname)s.directives'
  ];

  // mount on window for testing
  window.%(appname)s = angular.module('%(appname)s', requires);

  angular.module('%(appname)s').constant('AppSettings', require('./config'));

  angular.module('%(appname)s').config(require('./routes'));

  angular.module('%(appname)s').run(require('./on_run'));

  angular.bootstrap(document, ['%(appname)s']);

});
""" % {'appname': appname}

    @staticmethod
    def routes(appname):
        return """'use strict';

/**
 * @ngInject
 */
function Routes($stateProvider, $locationProvider, $urlRouterProvider) {

  $locationProvider.html5Mode(true);

  $stateProvider
    .state('Landing', {
      url: '/',
      controller: 'LandingCtrl as landing',
      templateUrl: 'partials/landing'
    });

  $urlRouterProvider.otherwise('/');

}

module.exports = Routes;
""" % {'appname': appname}

    @staticmethod
    def on_run(appname):
        return """'use strict';

/**
 * @ngInject
 */
function OnRun($rootScope, AppSettings) {

  // change page title based on state
  $rootScope.$on('$stateChangeSuccess', function(event, toState) {
    $rootScope.pageTitle = '';

    if ( toState.title ) {
      $rootScope.pageTitle += toState.title;
    }

    $rootScope.pageTitle += AppSettings.appTitle;
  });

}

module.exports = OnRun;
""" % {'appname': appname}

def partials(appname):
    return {
        'landing.html': """<div id="landing">
    <h3>%(appname)s has landed!</h3>
</div>
""" % {'appname': appname}
    }
    
class Styles(object):

    main = """/* Master Stylesheet */

// Libraries
@import '../../bower_components/fever/scss/fever';

// Components
@import 
  'base',
  'landing';
"""
    base = """/* Base Styles */
"""

    landing = """/* Landing Styles */
"""
