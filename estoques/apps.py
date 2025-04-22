from django.apps import AppConfig

class EstoquesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estoques'

    def ready(self):
        import estoques.signals  # Importa os sinais
