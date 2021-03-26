
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

from django.conf.urls.static import static


###########################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicaciones.urls')),
    path('publicaciones/', include('publicaciones.urls', namespace='home')),
    path('gestiones/', include('gestion.urls', namespace='gestiones')),
    path('usuarios/', include('usuarios.urls', namespace="usuarios")),
    path('api/', include('api.urls')),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
