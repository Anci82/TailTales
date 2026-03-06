from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic as views

from TailTales.accounts.forms import RegisterForm
from TailTales.accounts.models import Profile


class RegisterView(views.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')  # or 'pet-list' if you prefer

    def form_valid(self, form):
        response = super().form_valid(form)

        # Create Profile for the new user (no signals needed)
        Profile.objects.create(user=self.object)

        # Auto-login after registration
        login(self.request, self.object)
        return response