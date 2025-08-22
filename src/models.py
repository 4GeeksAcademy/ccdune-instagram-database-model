from flask_sqlalchemy import SQLAlchemy
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


class User(Base):
    __tablename__ = "user"

    ID: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    followers = relationship("Follower",
                             foreign_keys="[Follower.user_to_id]",
                             backref="followed",
                             cascade="all, delete-orphan")
    following = relationship("Follower",
                             foreign_keys="[Follower.user_from_id]",
                             backref="follower",
                             cascade="all, delete-orphan")      
    


    def serialize(self):
        return {
            "ID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }

    def __repr__(self):
        return f"<User {self.username}>"


class Follower(Base):
    """
    This is the new SQA 2.0 style:
    """
    __tablename__ = "follower"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.ID"), nullable=False)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.ID"), nullable=False)

    follower = relationship("User", foreign_keys=[user_from_id])
    followed = relationship("User", foreign_keys=[user_to_id])

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }

    def __repr__(self):
        return f"<Follower {self.user_from_id}>"


class Media(Base):
    __tablename__ = "media"

    ID: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.ID"), nullable=False)
    post = relationship("Post", backref="media")
    

    def serialize(self):
        return {
           "ID": self.ID,
           "type": self.type,
           "url": self.url,
           "post_id": self.post_id,
        }

    def __repr__(self):
        return f"<Media {self.ID}>"


class Post(Base):
    __tablename__ = "post"

    ID: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.ID"), nullable=False)
    user = relationship("User", back_populates="posts")
    media = relationship("Media", backref="post", cascade="all, delete-orphan")
    comments = relationship("Comment", backref="post", cascade="all, delete-orphan")        

    def serialize(self):
        return {
            "ID": self.ID,
            "user_id": self.user_id
        }

    def __repr__(self):
        return f"<Post {self.ID}>"


class Comment(Base):
    __tablename__ = "comment"

    ID: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.ID"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.ID"), nullable=False)

    author = relationship("User", backref="comments")
    post = relationship("Post", backref="comments")


    def serialize(self):
        return {
            "ID": self.ID,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id,
        }

    def __repr__(self):
        return f"<Comment {self.ID}>"
