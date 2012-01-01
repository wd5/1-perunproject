# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    #status = models.CharField('Статус', blank=True, max_length=50)
    location = models.CharField('Откуда', blank=True, max_length=50)
    about = models.TextField('О себе', blank=True)

    def __unicode__(self):
        return u"%s" % (self.user)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
User.get_profile = lambda u: UserProfile.objects.get_or_create(user=u)[0]
