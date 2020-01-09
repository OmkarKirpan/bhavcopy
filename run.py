import bhavcopy as bc
import cherrypy
import os


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'bhavcopy/public'
        }
    }

    cherrypy.quickstart(bc.controller.BhavController(), '/', conf)
