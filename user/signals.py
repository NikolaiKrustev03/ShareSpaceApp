from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == "user":

        superuser_group, _ = Group.objects.get_or_create(name='Superusers')
        staff_group, _ = Group.objects.get_or_create(name='Staff')

        post_model = apps.get_model('post', 'Post')
        comment_model = apps.get_model('comment', 'Comment')
        like_model = apps.get_model('like', 'Like')

        for model in [post_model, comment_model, like_model]:
            content_type = ContentType.objects.get_for_model(model)
            permissions = Permission.objects.filter(content_type=content_type)

            superuser_group.permissions.add(*permissions)

            staff_permissions = permissions.filter(codename__in=['add', 'view'])
            staff_group.permissions.add(*staff_permissions)
