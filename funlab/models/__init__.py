import mongoengine as me
from flask_mongoengine import MongoEngine

from .users import User
from .course import Course

__all__ = [
    "User",
    "Course"
    ]


db = MongoEngine()


def init_db(app):
    db.init_app(app)
