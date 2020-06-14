from .models import *
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
class customer(ModelForm):
	class Meta:
		model=profile
		fields='__all__'
		exclude=["user"]

	
