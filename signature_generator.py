#coding=utf-8
from __future__ import unicode_literals
import ConfigParser
import cherrypy
import gspread

class Home:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        self.key = config.get('spreadsheet', 'key')
        self.login = config.get('account', 'login')
        self.passwd = config.get('account', 'password')

    @cherrypy.expose
    def index(self, email=None):
        gc = gspread.login(self.login, self.passwd)
        wks = gc.open_by_key(self.key)
        worksheet = wks.get_worksheet(0)
        try:
            rownumber = worksheet.find(email).row
            return worksheet.row_values(rownumber)
        except:
            return "Not Found %s" % email

cherrypy.quickstart(Home())
