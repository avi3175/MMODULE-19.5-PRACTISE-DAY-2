from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from .forms import SignupForm
from django.contrib.auth import logout



from musician_app.models import Musician
from albums_app.models import Album




def home(request):
    combined_data = []

    albums = Album.objects.prefetch_related('musicians').all()
    
    for album in albums:
        for musician in album.musicians.all():
            combined_data.append({
                'id': musician.id,
                'musician_name': f"{musician.first_name}",
                'email': musician.email,
                'album_name': album.album_name,
                'release_date': album.release_date,
                'instrument_type': musician.instrument_type,
            })

    return render(request, 'base.html', {'combined_data': combined_data})

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})







def user_logout(request):
    logout(request)
    return redirect('login')




