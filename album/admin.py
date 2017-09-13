from django.contrib import admin

from .models import Album

#admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'put_time')
  list_filter = ('put_time', )

admin.site.register(Album, AlbumAdmin)