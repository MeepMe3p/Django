from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import LoginView
from blogs.models import Category
from .forms import CustomRegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class RegisterUser(generic.FormView):
    template_name = "users/register.html"
    form_class = CustomRegisterForm
    # form_class = CustomRegForm

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
class LoginUser(LoginView):
    # \https://www.pythontutorial.net/django-tutorial/django-loginview/

    template_name = 'users/login.html'
    # redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('blogs:CategoriesList') # if successful go to this urlname
    def form_invalid(self, form):
        messages.error(self.request,'Incorrect Username or Password')
        return self.render_to_response(self.get_context_data(form = form)) #create flash message then rerender
        
class CategoryList(generic.ListView):
    template_name = "blogs/categories.html"
    model = Category
    context_object_name = "turtles" # renames the object_list to this

class CategoryDetail(generic.DetailView):
    template_name = "blogs/detail.html"
    model = Category
    
    

