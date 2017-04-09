import webapp2
import handlers

app = webapp2.WSGIApplication([
    ('/?', handlers.FrontPage)
    ,('/([0-9]+)', handlers.Post)
    ,('/newpost', handlers.NewPost)
    ,('/signup', handlers.Signup)
    ,('/welcome', handlers.Welcome)
], debug=True)
