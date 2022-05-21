from j2fa_test.models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

