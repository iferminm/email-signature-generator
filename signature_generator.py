#coding=utf-8
from __future__ import unicode_literals
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('views'))
import ConfigParser
import cherrypy
import gspread

class SignatureGenerator:

    def serve_template(self, template_name, **kwargs):
        template = env.get_template(template_name)
        return template.render(**kwargs)

    @cherrypy.expose
    def index(self):
        return self.serve_template('what.html')

    @cherrypy.expose
    def how(self):
        return self.serve_template('how.html')

    @cherrypy.expose
    def why(self):
        return self.serve_template('why.html')


cherrypy.quickstart(SignatureGenerator(), '/', 'generator.cfg')
