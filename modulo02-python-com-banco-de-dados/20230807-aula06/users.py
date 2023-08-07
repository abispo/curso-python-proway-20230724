from database import session
from models import User, Profile


def list_users():
    return session.query(User).all()