from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import login_form, signup_form
from django.contrib import messages
from django.http.response import HttpResponseRedirect



# Create your views here.

class login(TemplateView):
    
    def get(self, request):
        form = login_form()
        return render(request, "login.html", {"form":form})

    def post(self, request):
        form = login_form(request.POST)
        if(form.is_valid()):
            print("Form is valid")
        else:
            print("Form is invalid")
        
        return redirect('/')

class signup(TemplateView):
    
    def get(self, request):
        form = signup_form()
        return render(request, "signup.html", {"form":form})

    def post(self, request):
        
        form = signup_form(request.POST)
        if(form.is_valid()):
            print("Form is valid")
            messages.success(request, 'Your profile has been saved. Please Login') 
            return HttpResponseRedirect("/")
        else:
            print("Form is invalid")
            return render(request, "signup.html", {'form':form})
        