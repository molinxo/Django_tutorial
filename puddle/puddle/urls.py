
from django.contrib import admin
from django.conf.urls.static import static, settings
from django.urls import path
from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
