from flask import render_template
from flask.views import MethodView

class Base(MethodView):
    def get(self, uri=None):
        return render_template('base.html')

class Partial(MethodView):
    def get(self, partial):
        return render_template('partials/%s.html' % partial)
