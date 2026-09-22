from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Track
# Create your views here.
def all_tracks(request):
  #{"id":1,"name":"python"}
  tracks=Track.objects.all().order_by('id')
  return render(request, 'tracks/list.html' , context={'tracks':tracks})

def get_tracks(request):
  return HttpResponse("<h1>Get Tracks Page</h1")

def tracks_insert(request):
   if request.method =='POST':
     name=request.POST['trname']
     Track.objects.create(name=name)
     return HttpResponse("<h>Inserted successfull</h1>") 
   return render(request, 'tracks/insert.html') 


def tracks_update(request, id):
    if request.method == 'POST':
        name = request.POST['trname']
        Track.objects.filter(id=id).update(name=name)
        #return redirect('/track/')
        return redirect('https://www.youtube.com/')
    
    context = {'track': Track.objects.get(id=id)}
    return render(request, 'tracks/update.html', context)
  

def tracks_delete(request ,id):
  Track.objects.filter(id=id).delete()
  return redirect('/track/')

