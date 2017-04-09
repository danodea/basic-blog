from basehandler import BaseHandler
from google.appengine.ext import db
from models import BlogPostModel

class Post(BaseHandler):
	def get(self, id):
		id = int(id)
		post = BlogPostModel.get_by_id(id)
		self.render("blog-post.html", subject=post.subject, content=post.content)