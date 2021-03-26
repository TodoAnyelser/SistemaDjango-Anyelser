from django.urls import path
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apiusuario',UsuariosViewSet)




urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]

urlpatterns += router.urls

#urlpatterns = format_suffix_patterns(urlpatterns)