from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Trainee
# Create your views here.

def all_trainee(request):
  context = {'trainees':Trainee.objects.all()}
  return render(request, 'trainee/list.html',context=context)

def get_trainee(request):
  return HttpResponse("<h1>Get Trainee Page</h1")

def trainee_insert(request):
  if request.method == 'POST':
    name = request.POST['trname']
    email = request.POST['tremail']
    image=request.FILES.get('trimage')
    Trainee.objects.create(name=name ,email=email ,image=image)
    return HttpResponse("<h1>Inserted successfully</h1>")
  return render(request,'insert.html') 

def trainee_update(request,id): 
  return HttpResponse(f"<h1>Update Trainee {id} Page</h1>") 

def trainee_delete(request,id):
  Trainee.objects.filter(id=id).update(status=False)
  return redirect('/trainee/')
