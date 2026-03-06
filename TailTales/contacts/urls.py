from django.urls import path

from TailTales.contacts.views import (
    ServiceContactCreateView,
    ServiceContactDeleteView,
    ServiceContactDetailView,
    ServiceContactListView,
    ServiceContactUpdateView,
)

urlpatterns = [
    path('', ServiceContactListView.as_view(), name='contact-list'),
    path('create/', ServiceContactCreateView.as_view(), name='contact-create'),
    path('<int:pk>/', ServiceContactDetailView.as_view(), name='contact-detail'),
    path('<int:pk>/edit/', ServiceContactUpdateView.as_view(), name='contact-edit'),
    path('<int:pk>/delete/', ServiceContactDeleteView.as_view(), name='contact-delete'),
]