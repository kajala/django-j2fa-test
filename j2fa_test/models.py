from django.contrib.auth.models import User
from django.db import models
from j2fa.helpers import j2fa_phone_filter


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', blank=True, on_delete=models.CASCADE)
    phone = models.CharField('phone number', max_length=32, db_index=True, blank=True, default='')
    require_2fa = models.BooleanField('2FA', blank=True, default=True)
    last_modified = models.DateTimeField('last modified', auto_now=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    def __str__(self):
        return "{}".format(self.id)

    @property
    def id(self):
        return self.user_id if self.user_id else None

    @property
    def phone_normalized(self):
        phone = j2fa_phone_filter(self.phone)
        if phone[:1] == '0':
            phone = '+358' + phone[1:]
        return phone

    def clean(self):
        self.phone = j2fa_phone_filter(self.phone)
