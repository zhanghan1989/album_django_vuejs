from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
  #return HttpResponse("welcome to my album")
  #return render(request, 'album/index.html', {'hello': 'hello, welcome to my album!'})
  album = models.Album.objects.get(pk=1)
  return render(request, 'album/index.html', {'album': album})