from django.apps import AppConfig

class CommunityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    # This name must match the exact string prefix of your app directory
    name = 'community' 
