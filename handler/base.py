import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    # def get(self,**template_variables):
    #     self.render("index.html",**template_variables)
    def get(self):
        self.render("index.html")
