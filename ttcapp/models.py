from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.utils import timezone


#id用
def create_id():
    return get_random_string(22)
# Create your models here.

class bento(models.Model):
    name = models.CharField(unique=True, max_length=64)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class be_left(models.Model):
    howmany_order = models.IntegerField(blank=True)
    name = models.ForeignKey(bento, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name.name+str(self.howmany_order)





class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(default=create_id, primary_key=True, max_length=22) 
    username = models.CharField(
        max_length=50, unique=True, blank=True, default='匿名')
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest poossible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class store_sale(models.Model):
    # id = models.CharField(primary_key=True, max_length=128)
    # user = models.CharField(blank=True, max_length=128)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    order_bento = models.IntegerField(blank=True)
    sold_bento = models.IntegerField(blank=True)
    morning_sale = models.IntegerField(blank=True)
    noon_sale = models.IntegerField(blank=True)
    payment = models.IntegerField(blank=True)
    be_left = models.ManyToManyField(be_left, related_name='be_left', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user) + str(self.created_at)
    

