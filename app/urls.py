from django.urls import path
from .views import CarViewSet
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cars',CarViewSet.as_view({'get':'list'}),name= 'cars'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)