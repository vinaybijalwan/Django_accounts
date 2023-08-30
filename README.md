# Django_accounts
Django version - 4.1

====> Creating Django user model with login from phone

##create a dir name django_accounts_website
$ mkdir django_accounts_website

$ cd django_accounts_website/

$ django-admin startproject website_accounts

$  cd website_accounts/
$ ls -a
  ./  ../  accounts/  manage.py*  website_accounts/


$ python manage.py startapp accounts

 --> add this app in setting.py file under INSTALLED_APPS
       'accounts',


$ cd accounts

$ ls -a 
   ./  ../  __init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py


open in vs code 

and work on models.py file


##########################################
from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomerUser(AbstractUser):
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number' #login with phone number
    REQUIRED_FIELDS = ['username']               ##while creating super user asking information
                                





#########################################

creating manager.py 

#################################
##its for createsuperuser, user 
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password = None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is Reqiured")

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
def create_superuser(self, phone_number, password = None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)
    
    return self.create_user(phone_number, password, **extra_fields)




##########################


add user model in setting.py files

AUTH_USER_MODEL = 'accounts.CustomerUser'


##Migrate 
python .\manage.py makemigrations

python .\manage.py migrate 

# now runserver 

python .\manage.py runserver


add user model to admin

admin.py 
###################################################
from django.contrib import admin
from .models import CustomerUser
# Register your models here.


admin.site.register(CustomerUser)


######################################################


now it look in admin page also

login with phone number and paswword

login - 9927012641
password - Vinay@1991
