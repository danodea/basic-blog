from basehandler import BaseHandler
import re

class Signup(BaseHandler):
    def get(self):
        self.render('blog-signup.html', errors=None)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        errors = {}

        if not self.validate_username(username):
            errors['username'] = "Please enter a valid username"

        if not self.validate_password(password):
            errors['password'] = "Please enter a valid password"

        if password != verify:
            errors['verify'] = "Passwords must match"

        if email and not self.validate_email(email):
            errors['email'] = "Please enter a valid email (or no email!)"

        if errors:
            self.render('blog-signup.html', username=username, email=email, errors=errors)
        else:
            self.response.headers.add('Set-Cookie', 'username=' + str(username) + '; Path=/')
            self.redirect('/welcome')

    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

    def validate_username(self, input):
        return self.USER_RE.match(input)

    def validate_password(self, input):
        return self.PASSWORD_RE.match(input)

    def validate_email(self, input):
        return self.EMAIL_RE.match(input)