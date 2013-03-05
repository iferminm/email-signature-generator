#coding=utf-8
from __future__ import unicode_literals
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('html'))
import ConfigParser
import cherrypy
import gspread

class SignatureGenerator:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        self.key = config.get('spreadsheet', 'key')
        self.login = config.get('account', 'login')
        self.passwd = config.get('account', 'password')

    def serve_template(self, template_name, **kwargs):
        template = env.get_template(template_name)
        return template.render(**kwargs)

    @cherrypy.expose
    def index(self, email=None):
        gc = gspread.login(self.login, self.passwd)
        wks = gc.open_by_key(self.key)
        worksheet = wks.get_worksheet(0)
        try:
            rownumber = worksheet.find(email).row
            return worksheet.row_values(rownumber)
        except:
            return self.serve_template('404.html')

cherrypy.quickstart(SignatureGenerator(), '/', 'generator.cfg')
