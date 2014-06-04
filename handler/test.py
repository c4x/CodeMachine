import random
import tornado.web
import tornado.websocket

def send_message(message,uuid,handlers):
    if uuid in handlers:
        handler = handlers[uuid]
        try:
            handler.write_message(message)
        except Exception as e:
            raise e

class TestIndexHandler(tornado.web.RequestHandler):
    def get(self):
        uuid = self.GenCRSF()
        self.render("testIndex.html",uuid = uuid)
        pass

    #使用时间戳生成，得到唯一
    def GenCRSF(length = 5):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.sample(chars, 4))

class TestHandler(tornado.web.RequestHandler):
    def post(self):
        test = self.get_argument('test')
        uuid = self.get_argument('uuid')
        print(uuid)
        send_message("ok,get test:{}".format(test),uuid,self.application.socketDict.handlers)
        self.finish()

class TestSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.application.socketDict.register(self,message)
        # send_message(message)


class SocketDict(object):
    def __init__(self):
        self.handlers = {}

    def register(self,socketHandler,uuid):
        self.handlers[uuid] = socketHandler
        pass
        
