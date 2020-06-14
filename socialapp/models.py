from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class profile(models.Model):
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=True,blank=True)
	profession = models.CharField(max_length=200,null=True,blank=True)
	thumb = models.ImageField(default='default.png',upload_to='media',null=True,blank=True)
	email = models.CharField(max_length=200,null=True,blank=True)
	phone = models.CharField(max_length=200,null=True,blank=True)

# Create your models here.
	def __str__(self):
		return str(self.name)


def create_profile(sender,instance,created,**kwargs):
	if created:
		profile.objects.create(user=instance)
		print('created')

post_save.connect(create_profile,sender=User)