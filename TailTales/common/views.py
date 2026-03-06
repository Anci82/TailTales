from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'common/home.html'


class AboutView(views.TemplateView):
    template_name = 'common/about.html'


class DashboardView(LoginRequiredMixin, views.TemplateView):
    template_name = 'common/dashboard.html'