from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name= 'website/login.html', authentication_form = LoginForm), name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name = 'contact'),
]
