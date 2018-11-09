import time
from django.contrib import admin

from appone.models import Album, Song, Artist

class PyPyMysicAdminSite(admin.AdminSite):
    site_header = 'PyPyMusic administration'

admin_site = PyPyMysicAdminSite(name='admin')

@admin.register(Album, site=admin_site)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('release_date',)
    list_display = ('name',
                    'artist',
                    'release_date', )

    autocomplete_fields = ('artist', )

@admin.register(Song, site=admin_site)
class SongAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ('lyrics',)

    list_display = ('name',
                    'album',
                    'duration_human_readable', )

    list_filter = ('album__name', 'album__artist__last_name')

    def duration_human_readable(self, obj):
        return time.strftime("%M:%S", time.gmtime(obj.duration))
    duration_human_readable.short_description = 'Duration'
    duration_human_readable.admin_order_field = 'duration'


@admin.register(Artist, site=admin_site)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'join_date',
        'published',
    )

    list_filter = ('published', )
    search_fields = [ 'full_name', ]

