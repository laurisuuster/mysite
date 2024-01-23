from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    # String representation of class 
    def __str__(self) -> str:
        return self.user.username

#OneToOneField because user can have 1 profile and profile can have 1 user
