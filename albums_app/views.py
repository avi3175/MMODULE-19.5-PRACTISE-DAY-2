from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.

def album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form = AlbumForm()
    return render(request,'./album.html',{'form':form})



def show_albums(request):
    albums = Album.objects.all()
    return render(request, './base.html', {'albums': albums})