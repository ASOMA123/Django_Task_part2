from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_trainee(request):
  trainee=[[1,"Asmaa"],[2,"sara"],[3,"mai"]]
  return render(request, 'trainee/list.html' , context={'trainees':trainee})

def get_trainee(request):
  return HttpResponse("<h1>Get Trainee Page</h1")

def trainee_insert(request):
  return HttpResponse("<h1>Insert Trainee Page</h1>") 

def trainee_update(request,id): 
  return HttpResponse(f"<h1>Update Trainee {id} Page</h1>") 

def trainee_delete(request,id):
  return HttpResponse(f"<h1>Delete Trainee {id} Page</h1>") 
