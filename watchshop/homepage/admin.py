from django.contrib import admin
from .models import Watches, WatcheUpload
# Register your models here.
admin.site.register(Watches)

#WatchUploads
class WatcheUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatcheUpload, WatcheUploadAdmin)

