from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('useradmin/', include('useradmin.urls')), 
    path('useradmin/', include('django.contrib.auth.urls')),
    path('browse/', include('modelclothing.urls')), 
    path('cart/', include('cart.urls')),
    path('customerservice/', include('customerservice.urls')), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)