import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from reclass.models.base import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, name
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Users must have an first name')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            **extra_fields
        )

        user.set_password(password)
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, name
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

"""
Inheriting the existing Abstract User
model and customizing
"""
class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    password_reset_required = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=35, blank=True, null=True, unique=True)
    password_reset_expiry = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)

    """
    Hidden fields (For reference) -
    password
    last_login
    """

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    """
    This methods are required in-built for django
    admin panel.
    """
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
