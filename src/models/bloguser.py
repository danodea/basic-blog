from google.appengine.ext import db

class BlogUser(db.Model):
    user = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
