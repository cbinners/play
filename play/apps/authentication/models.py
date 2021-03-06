from util.fields import ShortUUIDField
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, UserManager as DjangoUserManager
)


class UserManager(DjangoUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        return super()._create_user(username, email, password)


class User(AbstractBaseUser):
    id = ShortUUIDField(prefix="usr", max_length=128, primary_key=True)
    username = models.CharField(max_length=39, unique=True)
    email = models.CharField(max_length=512)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label = 'authentication'

    @property
    def is_admin(self):
        return self.username.lower() in ["dlsteuer", "joram", "brandonb927", "coldog", "matthieudolci", "codeallthethingz"]

    def assigned_to_team(self):
        from apps.tournament.models import TeamMember
        try:
            team = TeamMember.objects.get(user_id=self.id).team
            return True
        except TeamMember.DoesNotExist:
            pass

        return False
