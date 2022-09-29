from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    # reverse lazy finds the urls on demand
    template_name = 'accounts/signup.html'
# Create your views here.
