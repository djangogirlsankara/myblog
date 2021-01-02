from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        print('Installed Core app.')
        # You can add any hooks for the app here.
