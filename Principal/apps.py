from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PrincipalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Principal'
