from django.urls import path
from . import views
urlpatterns = [
    path('',views.album,name='album'),
    path('show_albums/', views.show_albums, name='show_albums'),
]
