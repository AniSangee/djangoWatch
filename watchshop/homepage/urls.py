from django.contrib import admin
from django.urls import path
from .views import Home, About, upload, Login, Signup, Logout, ShowProduct
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Home,name="home"),
    path('about/', About,name="about"),
    path('upload/', upload,name='upload'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', Logout,name='logout'),
    path('product/<int:id>', ShowProduct,name='product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
