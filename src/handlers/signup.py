from basehandler import BaseHandler
from utilities import validation

class Signup(BaseHandler):
    def get(self):
        self.render('blog-signup.html', errors=None)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        errors = {}

        if not validation.validate_username(username):
            errors['username'] = "Please enter a valid username"

        if not validation.validate_password(password):
            errors['password'] = "Please enter a valid password"

        if password != verify:
            errors['verify'] = "Passwords must match"

        if email and not validation.validate_email(email):
            errors['email'] = "Please enter a valid email (or no email!)"

        if errors:
            self.render('blog-signup.html', username=username, email=email, errors=errors)
        else:
            self.response.headers.add('Set-Cookie', 'username=' + str(username) + '; Path=/')
            self.redirect('/welcome')