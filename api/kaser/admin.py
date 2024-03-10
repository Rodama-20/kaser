from django.contrib import admin

from .models import Photo, Album

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "date_uploaded")
    search_fields = ("title", "album__title")
    list_filter = ("album", "date_uploaded")
    
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created")
    search_fields = ("title", "date_created")
    list_filter = ("date_created",)
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)