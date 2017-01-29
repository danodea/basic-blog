from basehandler import BaseHandler

class MainPage(BaseHandler):
	def get(self):
		self.write('hello world')