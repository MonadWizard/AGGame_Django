from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):

    def create_user(self,userid, user_username, user_email, password=None, user_country=None, user_state_divition=None, user_playing_city=None):
        if userid is None:
            raise TypeError('User ID should not be none')
        if user_username is None:
            raise TypeError('Users should have a username')
        if user_email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Password should not be none')

        user = self.model(userid=userid, user_username=user_username, user_email=self.normalize_email(user_email),
                        user_country=user_country, user_state_divition=user_state_divition, user_playing_city=user_playing_city)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,userid, user_username, user_email, password=None):
        if userid is None:
            raise TypeError('User ID should not be none')
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(userid, user_username, user_email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


user_roles = [
    ('Player', 'Player'),
    ('Scorekeeper', 'Scorekeeper'),
    ('Umpire', 'Umpire')
]


class User(AbstractBaseUser, PermissionsMixin):
    userid= models.CharField(primary_key=True,max_length=30, unique=True, db_index=True)
    user_username = models.CharField(max_length=100, unique=True, blank=True, null=True, db_index=True)
    # user_fullname = models.CharField(max_length=255, )
    user_fullname = models.JSONField(blank=True, null=True)
    user_dob = models.DateField(blank=True, null=True)
    user_email = models.EmailField(max_length=255, unique=True, db_index=True)
    user_callphone = models.CharField(max_length=30, unique=True, db_index=True, blank=True, null=True)
    user_country = models.CharField(max_length=200, blank=True, null=True)
    user_state_divition = models.CharField(max_length=200, blank=True, null=True)
    user_playing_city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_photopath = models.CharField(max_length=200, blank=True, null=True)
    user_life_history = models.JSONField(blank=True, null=True)
    user_playing_sports = models.JSONField(blank=True, null=True)
    user_interested_sports = models.JSONField(blank=True, null=True)
    user_configuration = models.JSONField(blank=True, null=True)
    user_device_info = models.JSONField(blank=True, null=True)
    user_type_flag = ArrayField(models.CharField(max_length=200,choices=user_roles), default=list, blank=True, null=True)

    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_created_at = models.DateTimeField(auto_now_add=True)
    # user_updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['userid','user_username']

    objects = UserManager()

    def __str__(self):
        return self.user_email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }





