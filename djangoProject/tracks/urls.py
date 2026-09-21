from django.contrib import admin
from django.urls import path , include
from .views import *
#tracks
urlpatterns = [
path('' , all_tracks),
path('insert/',tracks_insert, name='insert_track' ),
path('id/',get_tracks),
path('update/<int:id>',tracks_update, name='update_track' ),
path('delete/<int:id>', tracks_delete , name='delete_track'),
]