from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
  #return HttpResponse("welcome to my album")
  #return render(request, 'album/index.html', {'hello': 'hello, welcome to my album!'})
  #album = models.Album.objects.get(pk=1)
  #return render(request, 'album/index.html', {'album': album})
  albums = models.Album.objects.all()
  return render(request, 'album/index.html', {'albums': albums})

def album_page(request, album_id):
  album = models.Album.objects.get(pk=album_id)
  return render(request, 'album/album_page.html', {'album': album})

# def album_edit_page(request):
#   return render(request, 'album/album_edit_page.html')
def album_edit_page(request, album_id):
  if str(album_id) == '0':
    return render(request, 'album/album_edit_page.html')
  album = models.Album.objects.get(pk=album_id)
  return render(request, 'album/album_edit_page.html', {'album': album})

# def album_edit_action_page(request):
#   title = request.POST.get('title', 'TITLE')
#   content = request.POST.get('content', 'CONTENT')
#   models.Album.objects.create(title=title, content=content)
#   albums = models.Album.objects.all()
#   return render(request, 'album/index.html', {'albums': albums})
def album_edit_action_page(request):
  title = request.POST.get('title', 'TITLE')
  content = request.POST.get('content', 'CONTENT')
  album_id = request.POST.get('album_id', '0')

  if album_id == '0':
    models.Album.objects.create(title=title, content=content)
    albums = models.Album.objects.all()
    return render(request, 'album/index.html', {'albums': albums})
  album = models.Album.objects.get(pk=album_id)
  album.title = title
  album.content = content
  album.save()
  
  return render(request, 'album/album_page.html', {'album': album})



