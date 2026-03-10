from django.urls import path
from TailTales.care.views import (
    AppointmentListView, AppointmentCreateView, AppointmentDetailView,
    AppointmentUpdateView, AppointmentDeleteView,
    PreventiveCareListView, PreventiveCareCreateView, PreventiveCareDetailView,
    PreventiveCareUpdateView, PreventiveCareDeleteView, PreventiveCareMarkGivenView,
    AppointmentListApiView, AppointmentDetailApiView,
)

urlpatterns = [
    path('api/appointments/', AppointmentListApiView.as_view(), name='api-appointment-list'),
    path('api/appointments/<int:pk>/', AppointmentDetailApiView.as_view(), name='api-appointment-detail'),

    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment-edit'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),

    path('preventive/', PreventiveCareListView.as_view(), name='preventivecare-list'),
    path('preventive/create/', PreventiveCareCreateView.as_view(), name='preventivecare-create'),
    path('preventive/<int:pk>/', PreventiveCareDetailView.as_view(), name='preventivecare-detail'),
    path('preventive/<int:pk>/edit/', PreventiveCareUpdateView.as_view(), name='preventivecare-edit'),
    path('preventive/<int:pk>/delete/', PreventiveCareDeleteView.as_view(), name='preventivecare-delete'),
    path('preventive/<int:pk>/mark-given/', PreventiveCareMarkGivenView.as_view(), name='preventivecare-mark-given'),
]