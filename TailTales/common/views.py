from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from datetime import timedelta
from django.utils import timezone

from TailTales.care.models import Appointment

def get_tomorrows_appointments(user):
    tomorrow = timezone.localdate() + timedelta(days=1)

    return (
        Appointment.objects
        .filter(
            pet__owner=user,
            date=tomorrow,
            is_completed=False,
        )
        .select_related('pet', 'service_contact')
        .order_by('pet__name', 'title')
    )

class HomeView(views.TemplateView):
    template_name = 'common/home.html'


class AboutView(views.TemplateView):
    template_name = 'common/about.html'


class DashboardView(LoginRequiredMixin, views.TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tomorrow_appointments'] = get_tomorrows_appointments(self.request.user)
        return context

