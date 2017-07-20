from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
import os 

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class MyUserManager(UserManager):
	def create_MyUser(self,input):
		user = self.create(username=input['user_name'],first_name=input['first_name'],last_name=input['last_name'],email=input['email'])
		return user

		
class MyUser(AbstractUser):
	defaultBlog = models.IntegerField(null=True)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	objects=MyUserManager()
	def __str__(self):
		return self.username