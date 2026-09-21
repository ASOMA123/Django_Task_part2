from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_myuser(request):
  myuser=[[1,"Toyota"],[2,"BMW"],[3,"Tesla"]]
  return render(request, 'myuser/list.html' , context={'myusers':myuser})


def login(request):
  return HttpResponse("<h1>Login Page</h1>") 

def signup(request): 
  return HttpResponse("<h1>Signup Page</h1>") 

def logout(request):
  return HttpResponse("<h1>Logout Page</h1>") 

def myuser_insert(request):
  return HttpResponse("<h1>Insert Myuser Page</h1>") 

def myuser_update(request,id): 
  return HttpResponse(f"<h1>Update Myuser {id} Page</h1>") 

def myuser_delete(request,id):
  return HttpResponse(f"<h1>Delete Myuser {id} Page</h1>") 
