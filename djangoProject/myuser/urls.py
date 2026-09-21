from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ 
  path('',all_myuser),
  path('login/',login ),
  path('sinup/',signup ),
  path('logout/',logout ),
  path('insert/',myuser_insert,name='insert_myuser'),
  path('update/<int:id>',myuser_update, name='update_myuser' ),
  path('delete/<int:id>', myuser_delete , name='delete_myuser'),

]