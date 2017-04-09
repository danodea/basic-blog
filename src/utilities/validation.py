import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def validate_username(input):
    return USER_RE.match(input)

def validate_password(input):
    return PASSWORD_RE.match(input)

def validate_email(input):
    return EMAIL_RE.match(input)