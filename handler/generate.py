import tornado.web
import tornado.websocket
import util.generatePojo as generatePojo

def send_message(message,uuid,handlers):
    if uuid in handlers:
        handler = handlers[uuid]
        try:
            handler.write_message(message)
        except Exception as e:
            raise e

class GenerateHandler(tornado.web.RequestHandler):
    def post(self):
        user = self.get_argument('user')
        password = self.get_argument('password')
        host = self.get_argument('host')
        db = self.get_argument('db')
        tables = self.get_arguments("tables")
        uuid = self.get_argument('uuid')
        for table in tables:
            generatePojo.generate(table, user, password, host, db)
            send_message("finish table:{}".format(table),uuid,self.application.socketDict.handlers)
        send_message("close",uuid,self.application.socketDict.handlers)
        self.finish()


class GenerateSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.application.socketDict.register(self,message)

class SocketDict(object):
    def __init__(self):
        self.handlers = {}

    def register(self,socketHandler,uuid):
        self.handlers[uuid] = socketHandler
        pass