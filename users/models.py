from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        """
        Create and saves a user with the given email, d.o.b and password
        """
        if not email:
            raise ValueError("User must have an email address")
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, first_name, last_name, email, password=None):
        """
        Creates ans save superuser with given email d.o.b and user
        """
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password
            
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email







