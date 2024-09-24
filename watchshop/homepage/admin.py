from django.contrib import admin
from .models import Watches, WatchUpload,Wishlists,Carts
# Register your models here.
admin.site.register(Watches)

#WatchUploads
class WatchUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchUpload, WatchUploadAdmin)

admin.site.register(Wishlists)
admin.site.register(Carts)
