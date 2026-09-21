from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_tracks(request):
  tracks=[[1,"Odoo"],[2,"Python"],[3,"Django"]]
  return render(request, 'tracks/list.html' , context={'tracks':tracks})

def get_tracks(request):
  return HttpResponse("<h1>Get Tracks Page</h1")

def tracks_insert(request):
  return HttpResponse("<h1>Insert Tracks Page</h1>") 

def tracks_update(reques,id):
  return HttpResponse(f"<h>Update Tracks {id} Page</h1>") 

def tracks_delete(request ,id):
  return HttpResponse(f"<h1>Delete Tracks {id} Page</h1>") 
