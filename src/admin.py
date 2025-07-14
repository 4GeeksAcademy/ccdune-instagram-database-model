import os
from flask_admin import Admin
from models import db, User, Follower, Media, Post, Comment
from flask_admin.contrib.sqla import ModelView


class FollowerView(ModelView):
    column_list = [
        'user_from_id', 'user_to_id'
    ]


class UserView(ModelView):
    column_list = [
        'ID', 'username', 'firstname', 'lastname', 'email'
    ]

class MediaView(ModelView):
    column_list = [
        'ID', 'type', 'url', 'post_id'
    ]

class PostView(ModelView):
    column_list = [
        'ID', 'user_ID'
    ]

class CommentView(ModelView):
    column_list = [
        'ID', 'comment_text', 'author_id', 'post_id'
    ]


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(FollowerView(Follower, db.session))
    admin.add_view(UserView(User, db.session))
    admin.add_view(MediaView(Media, db.session))
    admin.add_view(PostView(Post, db.session))
    admin.add_view(CommentView(Comment, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
