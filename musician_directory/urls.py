from django.urls import path,include
from django.contrib import admin
from .views import home, SignupView, CustomLoginView, profile,user_logout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/',user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('musician/',include('musician_app.urls')),
    path('album/',include('albums_app.urls')),
    # path('show-all-data/',show_all_data, name='show_all_data'),
]

