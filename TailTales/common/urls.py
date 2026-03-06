from django.urls import path

from TailTales.common.views import HomeView, AboutView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]