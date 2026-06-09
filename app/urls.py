from django.urls import path
from .views import CarViewSet,CarDetailView,CarListCreateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cars',CarViewSet.as_view({'get':'list'}),name= 'cars'),
    path('cars/', CarListCreateView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)