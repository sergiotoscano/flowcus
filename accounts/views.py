from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import forms


class SignupView(CreateView):
    form_class = forms.SignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class PasswordChangeDoneView(TemplateView):
    template_name = 'accounts/password_change_done.html'

class PasswordResetDoneView(TemplateView):
    template_name = 'accounts/password_reset_done.html'
