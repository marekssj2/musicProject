from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    # success_url = reverse_lazy('music:index')


# Dodawanie muzyki do albumu

class MusicCreate(CreateView):
    model = Song
    fields = ['album','song_title','file_type', 'audio_file']

class MusicDelete(DeleteView):
    model = Song
    # success_url = reverse_lazy('music:detail',kwargs={'pk': model.get_absolute_url})



#
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'music/registration_form.html'
#
#     # Display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form':form})
#
#     # Proces form data
#     # Po naciśnięciu przycisku submit.
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # return User object if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('music:index')
#
#         return render(request, self.template_name, {'form':form})
































# from django.shortcuts import get_object_or_404, render
# from .models import Album,Song
# # Create your views here.
#
# def index(request):
#     all_albums = Album.objects.all()
#     return render(request, 'music/index.html', {'all_albums': all_albums})
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#         'album': album,
#         'error_message':'You did not select a valid song',
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})
