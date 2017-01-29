import webapp2
import handlers

app = webapp2.WSGIApplication([
    ('/', handlers.MainPage)
], debug=True)
