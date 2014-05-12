import sys
# sys.setdefaultencoding("utf8")
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import handler.base
import handler.database

define("port", default = 8080, help = "run on the given port", type = int)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            login_url = "/",
            debug = True
        )

        handlers = [
            (r"/", handler.base.IndexHandler),
            (r"/getDatabases",handler.database.DatabaseHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    # tornado.autoreload.start(loop) 
    # loop.start()

if __name__ == "__main__":
    main()
