from django.apps import AppConfig
from django.db.models.signals import post_migrate


def ensure_admin_user(sender, **kwargs):
    from django.contrib.auth import get_user_model
    from django.conf import settings
    User = get_user_model()
    username = 'nk28'
    password = settings.BOT_ADMIN_PASS or 'nom'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email='', password=password)


class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'

    def ready(self):
        post_migrate.connect(ensure_admin_user, sender=self)
