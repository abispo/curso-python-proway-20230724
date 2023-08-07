# main.py

from database import engine, Base

from models import User, Profile, Post


if __name__ == "__main__":

    Base.metadata.create_all(engine)
