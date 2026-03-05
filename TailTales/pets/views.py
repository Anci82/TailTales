from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic as views

from TailTales.pets.forms import PetCreateForm, PetEditForm
from TailTales.pets.models import Pet


class PetListView(LoginRequiredMixin, views.ListView):
    model = Pet
    template_name = 'pets/pet-list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)


class PetCreateView(LoginRequiredMixin, views.CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-create.html'
    success_url = reverse_lazy('pet-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PetDetailView(LoginRequiredMixin, views.DetailView):
    model = Pet
    template_name = 'pets/pet-detail.html'
    context_object_name = 'pet'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)


class PetUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit.html'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('pet-detail', kwargs={'pk': self.object.pk})


class PetDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = 'pets/pet-delete.html'
    success_url = reverse_lazy('pet-list')

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)
