from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import customer

def home(request):
	return render(request,'user/home.html',{})

def profile(request):
	if request.user.is_authenticated:
		
		return render(request,'user/profile.html',{})
	else:
		return redirect('user_home')

def login_user(request):
	if request.user.is_authenticated:
		return render(request, 'user/home.html')
	else:
		if request.method == 'POST':
			username=request.POST.get("username")
			password=request.POST.get("password")
			user= authenticate(request,username=username,password=password)
			if user:
				if user.is_active:
					
					login(request,user)
					return render(request, 'user/home.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'user/login.html', context)


def signup(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('user_home')
		else:
			messages.info(request, 'Password is not valid')
	else:
		form = UserCreationForm()
	return render(request,'user/signup.html',{'form':form})


def userpage(request):
	if not request.user.is_authenticated:
		return redirect('user_home')
	else:
		profile=request.user.profile
		form= customer(instance=profile)
		
		if request.method=='POST':
			form = customer(data=request.POST,instance=profile)
			form1= request.FILES
			
			if form.is_valid():
				user=form.save(commit=False)
				

				if 'thumb' in form1:
					user.thumb=form1["thumb"]
				user.save()
				
				
				
				return render(request,'user/userpage.html',{'form':form})

					
					
		return render(request,'user/userpage.html',{'form':form})
		# Create your views here.




def logout_user(request):
	logout(request)
	return redirect('user_home')
