from django.contrib import admin
from django.urls import path,include
from socialapp import views
from django.conf.urls import url

urlpatterns = [
	path('',views.home,name='user_home'),
	path('signup',views.signup,name='signup'),
	path('login',views.login_user,name='login'),
	path('profile',views.profile,name='profile'),
	path('userpage',views.userpage,name='userpage'),
	path('logout_user',views.logout_user,name='logout_user'),

]
