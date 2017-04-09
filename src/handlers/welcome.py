from basehandler import BaseHandler

class Welcome(BaseHandler):
    def get(self):
        self.render('blog-welcome.html', username=self.request.cookies.get('username'))