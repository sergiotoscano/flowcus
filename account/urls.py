from django.urls import path
from django.contrib.auth import views as auth_views #changing name to not mess up the import views below
from . import views


app_name = 'account'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
]

