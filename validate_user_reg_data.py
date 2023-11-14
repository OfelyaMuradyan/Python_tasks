import re
def validate_username_f(us_name):
    if len(us_name) >= 5 and len(us_name) <= 20 and us_name.isalnum():
        ls = ['admin', 'root', 'user']
        for i in ls:
            if i in us_name.lower():
                return False
        return True
    return False

def validate_email_f(email):
    if email[len(email) - 10:] == "@gmail.com" and email.count('@') == 1:
        return True
    return False

def validate_phone_f(num):
    phone_num =  r'^(\+\d{1,13}|\d{9})$'
    return re.match(phone_num, str(num)) is not None 

def validate_pass_f(passwd):
    if len(passwd) >= 8 and any(char.isupper() for char in passwd):
        if any(char.islower() for char in passwd) and any(char.isdigit() for char in passwd):
            if any(char in ".!@#$%^&*" for char in passwd):
                return True
    return False

def validate_re_pass_f(passwd1, passwd2):
    if passwd1 == passwd2:
        return True
    return False


def validate_username(func):
    def wrapper(*args):
        if not validate_username_f(args[0]):
            print("Invalid username")
            return
        return func(*args)
    return wrapper


def validate_email(func):
    def wrapper(*args):
        if not validate_email_f(args[1]):
            print("Invalid email")
            return
        return func(*args)
    return wrapper


def validate_phone(func):
    def wrapper(*args):
        if not validate_phone_f(args[2]):
            print("Invalid phone number")
            return
        return func(*args)
    return wrapper


def validate_pass(func):
    def wrapper(*args):
        if not validate_pass_f(args[3]):
            print("Invalid password")
            return
        return func(*args)
    return wrapper


def validate_re_pass(func):
    def wrapper(*args):
        if not validate_re_pass_f(args[3], args[4]):
            print("Repeated password is not true")
            return
        return func(*args)
    return wrapper

@validate_re_pass
@validate_pass
@validate_phone
@validate_email
@validate_username
def register_user(username, email, phone, passwd, re_pass):
    print("Success")

register_user('dgdgdgd', 'sfsfsf@gmail.com', '+37499456467', 'fgdgfAA2@', 'fgdgfAA2@')