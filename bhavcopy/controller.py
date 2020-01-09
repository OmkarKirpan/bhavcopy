import cherrypy
import re
import jinja2
from datetime import datetime, timedelta

from bhavcopy import bse


class BhavController(object):
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader('bhavcopy', 'res/templates'),
        autoescape=jinja2.select_autoescape(['html', 'xml'])
    )

    @cherrypy.expose
    def index(self, date_str=None):

        if date_str is None:
            date = datetime.today() - timedelta(1)
        else:
            date = datetime.strptime(date_str, '%d%m%y')

        try:
            equities = bse.fetch_bhav(date)
        except bse.BhavNotFoundException:
            return "Bhav not found on BSE for " + date.strftime('%d-%m-%y') + ". Try with another date."

        for equity in equities:
            print(equity.name + " " + str(equity.open) + " " + repr(equity.date))

        return "OK."
