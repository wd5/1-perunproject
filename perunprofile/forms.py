from django.db import models
from django.forms import ModelForm
from perunprofile.models import UserProfile
 
class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user', 'status',)
