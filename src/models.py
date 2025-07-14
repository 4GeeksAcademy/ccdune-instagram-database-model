from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    String, Column, Table, ForeignKey,
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped,
    mapped_column, relationship,
)

class Base(DeclarativeBase):
    """
    This is magic that can be ignored
    for now!  It's a special tool
    that will help us later.
    """


db = SQLAlchemy(model_class=Base)

class Follower(Base):
    """
    This is the new SQA 2.0 style:
    """
    __tablename__ = "follower"

    user_from_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_to_id: Mapped[str] = mapped_column(unique=True, nullable=False)


    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }

    def __repr__(self):
        return f"<Follower {self.user_from_id}>"
    
class User(Base):
    __tablename__ = "user"

    ID: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

    def __repr__(self):
        return f"<User {self.ID}>"
    
class Media(Base):
    __tablename__ = "media"

    ID: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[enumerate] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "type": self.type,
            "url": self.url,
            "lastname": self.lastname,
            "post_id": self.post_id
        }

    def __repr__(self):
        return f"<User {self.ID}>"
    

class Post(Base):
    __tablename__ = "post"

    ID: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[enumerate] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "user_id": self.user_id
        }

    def __repr__(self):
        return f"<User {self.ID}>"



class Comment(Base):
    __tablename__ = "comment"

    ID: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "ID": self.ID,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "lastname": self.lastname,
            "post_id": self.post_id
        }

    def __repr__(self):
        return f"<User {self.ID}>"