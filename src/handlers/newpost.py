from basehandler import BaseHandler
from models import BlogPostModel

class NewPost(BaseHandler):
	def render_page(self, subject='', content='', error=''):
		self.render('blog-newpost.html', subject=subject, content=content, error=error)

	def get(self):
		self.render_page()

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')

		if not (subject and content):
			self.render_page(subject=subject, content=content, error="Please submit both a subject and content")
		else:
			post = BlogPostModel(subject=subject, content=content)
			post.put()
			id = str(post.key().id())
			self.redirect('/' + id)
