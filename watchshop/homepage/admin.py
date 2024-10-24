from django.contrib import admin
from .models import Watches,WatchUpload,Wishlist,Cart,CartItem,WatchReview
# Register your models here.
admin.site.register(Watches)


#WatchUploads
class WatchUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image','count')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchUpload, WatchUploadAdmin)
# wishlist
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ('user', 'products')
#     list_filter = ('user', 'products')
# admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Wishlist)
# cart
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'products')
#     list_filter = ('user', 'products')
# admin.site.register(Cart,CartAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)


#WatchReview
class WatchReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'rating')
    list_filter = ('rating', 'product')
admin.site.register(WatchReview, WatchReviewAdmin)