from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView,LogoutView as AuthLogoutView

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

class CustomLoginView(AuthLoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

#ログインできたら移るurlを指定
    def get_success_url(self):
        return reverse_lazy('todo:list')

class CustomLogoutView(AuthLogoutView):
    template_name = 'registration/logout.html'




