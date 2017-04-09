from basehandler import BaseHandler
from google.appengine.ext import db
from models import BlogPostModel

class FrontPage(BaseHandler):
	def get(self):
		posts = db.GqlQuery("SELECT * FROM BlogPostModel ORDER BY created DESC")
		self.render('blog-front.html', posts=posts)