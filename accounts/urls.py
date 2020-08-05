from django.urls import path, re_path
from django.contrib.auth import views as auth_views #changing name to not mess up the import views below
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view()),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
                                                                email_template_name='accounts/password_reset_email.html',
                                                                subject_template_name='accounts/password_reset_subject.txt',
     #                                                           success_url='accounts/login',
                                                                from_email='noreply@flowcus.com',
                                                                ), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view()),
    re_path('reset/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html')),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')),
    
#    http://127.0.0.1:8000/accounts/reset/MzE/5ir-73d1323d6c4de43a4374/
 #   {{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
]

