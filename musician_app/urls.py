from django.urls import path
from . import views
urlpatterns = [
    path('',views.musician,name='musician'),
    path('show_musicians/', views.show_musicians, name='show_musicians'),
    path('musician/edit/<int:id>/', views.edit, name='edit_musician'),
    path('musician/delete/<int:id>/',views.delete, name='delete_musician'),

]
