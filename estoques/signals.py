from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import Profile

# Sinal para criar ou atualizar o perfil do usuário
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# Sinal para registrar informações de login
@receiver(user_logged_in)
def save_login_info(sender, request, user, **kwargs):
    print(f"Usuário {user.username} fez login!")
    # Atualizar o horário do último login
    user.last_login = now()
    user.save()