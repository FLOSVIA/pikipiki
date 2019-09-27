'''from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, username, password, email):
        if not username:
            raise ValueError('Users must have an username')
        print(username,password,email)

        user = self.model(
            username=username,  
            password=password,
            email= email,
            #self.normalize_email(email),
            #userID=models.AutoField(primary_key=True)
        )
        #user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    EmailField(
        verbose_name='email',
        max_length=255
    )
    userID=models.AutoField(primary_key=True, auto_created=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
'''