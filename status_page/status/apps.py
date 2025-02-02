from django.apps import AppConfig

class StatusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'status'

    def ready(self):
        import status.signals  # Import signals when the app is ready
