
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_view

app_name = 'myapp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.hom,name="home"),
    # path('register/',views.register,name='register'),
    path('signup/',views.signuppage,name='signup'),
    # path('login/',views.loginpage,name='login'),
    path('login/', auth_view.LoginView.as_view(template_name="forms/login.html"), name='login'),
    # path('logout/', auth_view.LogoutView.as_view(template_name="forms/logout.html"), name='logout'),
    
    path('signout/',views.signout,name='signout'),
    path('profile/', views.profile,name='profile'),
    path('profile/update', views.profile_update,name='profile_update'),   
]

    

