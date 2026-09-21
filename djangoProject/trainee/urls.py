from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
#trainee
    path('',all_trainee),
    path('insert/',trainee_insert,name='insert_trainee'),
    path('get/<int:id>',get_trainee ),
    path('update/<int:id>',trainee_update, name='update_trainee' ),
    path('delete/<int:id>', trainee_delete , name='delete_trainee'),
]

