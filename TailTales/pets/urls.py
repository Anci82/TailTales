from django.urls import path

from TailTales.pets.views import (
    PetCreateView,
    PetDeleteView,
    PetDetailView,
    PetGalleryView,
    PetListView,
    PetUpdateView,
)

urlpatterns = [
    path('', PetListView.as_view(), name='pet-list'),
    path('create/', PetCreateView.as_view(), name='pet-create'),
    path('gallery/', PetGalleryView.as_view(), name='pet-gallery'),
    path('<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('<int:pk>/edit/', PetUpdateView.as_view(), name='pet-edit'),
    path('<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),
]