import cherrypy
import re
import jinja2
from datetime import datetime, timedelta

from bhavcopy import bse, worker


class BhavController(object):
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader('bhavcopy', 'res/templates'),
        autoescape=jinja2.select_autoescape(['html', 'xml'])
    )

    @cherrypy.expose
    def index(self, row_size=10, date_str=None, error=None):

        if date_str is None:
            date = datetime.today() - timedelta(1)
        else:
            date = datetime.strptime(date_str, '%d%m%y')

        date_text = date.strftime('%d, %B %Y')

        try:
            equities = worker.DAO().get_equities(date=date)
        except worker.RedisDataNotFoundException:
            raise cherrypy.HTTPError(message="Data not found in database")

        for equity in equities[:row_size]:
            print(equity.name + " " + str(equity.open) + " " + repr(equity.date))
        return "OK."

    @cherrypy.expose
    def update(self, date_str=None):

        if date_str is None:
            date = datetime.today() - timedelta(1)
        else:
            date = datetime.strptime(date_str, '%d%m%y')

        try:
            equities = bse.fetch_bhav(date)
        except bse.BhavNotFoundException:
            return "Bhav not found on BSE for " + date.strftime('%d-%m-%y') + ". Try with another date."
        dao = worker.DAO()
        for equity in equities:
            print(equity.name + " " + str(equity.open) + " " + repr(equity.date))
            dao.insert_equity(equity)

        return "OK."
