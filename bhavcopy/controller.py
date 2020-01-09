import cherrypy
import re
import jinja2
from datetime import datetime, timedelta

from bhavcopy import bse, worker


class BhavController(object):
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader('bhavcopy', 'public/templates'),
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

        template = self.jinja.get_template('index.html')
        return template.render(equities=equities[:row_size], allequities=equities, date=date_text, error=error)

    @cherrypy.expose
    def detail(self, name, row_size=10, date_str=None):

        name = name.upper()
        if re.search(r'[^A-Z .&-]', name) is not None:
            return self.index(error="Illegal stock name %s." % name)

        try:
            equities = worker.DAO().get_equities(name=name)
        except worker.RedisDataNotFoundException:
            return self.index(error=name + " was not found in our database. Please search for a different name.")

        equities.sort(key=lambda eq: eq.date, reverse=True)

        # get allequities for search
        if date_str is None:
            date = datetime.today() - timedelta(1)
        else:
            date = datetime.strptime(date_str, '%d%m%y')

        try:
            allequities = worker.DAO().get_equities(date=date)
        except worker.RedisDataNotFoundException:
            raise cherrypy.HTTPError(message="Data not found in database")

        template = self.jinja.get_template('detail.html')
        return template.render(equities=equities[:row_size], allequities=allequities)

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
