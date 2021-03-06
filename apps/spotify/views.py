from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
        return render(request, 'spotify/home.html', {})

def top_songs(request):
    try:
        lista = Song.objects.order_by('views').reverse()[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("Error, lista vacia.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':lista})

def playlist_view(request):
    user = Spotify_User.get_user(request)
    if user is not None:
        playlists = user.get_playlists()
    else:
        playlists = Playlist.objects.all()
    return render(request, 'spotify/playlists.html', {'playlist_list':playlists})

def profile(request):
    app_user = Spotify_User.get_user(request)
    return render(request, 'spotify/profile.html', {'usuario':app_user})

def log_out(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'spotify/logout.html', {})
