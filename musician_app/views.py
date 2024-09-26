# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import MusicianForm

# @login_required
# def musician(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = MusicianForm()

#     return render(request, './musician.html', {'form': form,'user': request.user})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MusicianForm
from .models import Musician

@login_required
def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST, user=request.user)  # Pass user=request.user here
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = MusicianForm(user=request.user)  # Pass user=request.user here

    return render(request, 'musician.html', {'form': form, 'user': request.user})



def show_musicians(request):
    musicians = Musician.objects.all()
    return render(request, './base.html', {'musicians': musicians})


def edit(request,id):
    edit_music = Musician.objects.get(pk=id)
    form = MusicianForm(instance=edit_music)
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    

    return render(request,'./musician.html',{'form':form})


def delete(request,id):
    delete_music = Musician.objects.get(pk=id)
    delete_music.delete()
    return redirect('homepage')