from django.apps import apps
import importlib


def import_model(app_label, model_name):
    try:
        return apps.get_model(app_label, model_name)
    except LookupError as e:
        raise ImportError(f"Cannot import model '{model_name}' from app '{app_label}'. {e}")


def get_user_model():
    return import_model('user', 'User')


def get_post_model():
    return import_model('post', 'Post')


def get_comment_model():
    return import_model('comment', 'Comment')


def get_like_model():
    return import_model('like', 'Like')


def get_board_model():
    return import_model('board', 'Board')


def import_form(app_label, form_name):
    try:
        module_path = f"{app_label}.forms"
        module = importlib.import_module(module_path)
        return getattr(module, form_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Cannot import form '{form_name}' from app '{app_label}'. {e}")


def get_user_form():
    return import_form('user', 'UserForm')


def get_post_form():
    return import_form('post', 'PostForm')


def get_comment_form():
    return import_form('comment', 'CommentForm')


def get_like_form():
    return import_form('like', 'LikeForm')


def get_board_form():
    return import_form('board', 'BoardForm')
