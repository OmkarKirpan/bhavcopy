import bhavcopy as bc
import cherrypy
import os


# bcopy = bc.controller.fetch_bhav()

# print(dir(bcopy[0]))


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    # res_path = os.path.join(os.path.dirname(__file__), 'res/')

    cherrypy.quickstart(bc.controller.BhavController(), '/', conf)
