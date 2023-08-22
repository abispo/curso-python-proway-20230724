from django.contrib.auth.models import User
from django.db.models import Q

def dados_preenchidos(*args):
    return all(args)


def username_ou_email_ja_existem(username, email):
    # SELECT * FROM auth_user WHERE username = '<username>' OR email = '<email>'
    return User.objects.filter(Q(username=username) | Q(email=email)).all()
