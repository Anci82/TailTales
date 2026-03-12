from django.urls import path

from TailTales.common.views import HomeView, AboutView, DashboardView, HowItWorksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('how-it-works/', HowItWorksView.as_view(), name='how-it-works'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]