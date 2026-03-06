from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from TailTales.contacts.forms import ServiceContactForm
from TailTales.contacts.models import ServiceContact


class ServiceContactListView(LoginRequiredMixin, views.ListView):
    model = ServiceContact
    template_name = 'contacts/contact-list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return ServiceContact.objects.filter(owner=self.request.user)


class ServiceContactCreateView(LoginRequiredMixin, views.CreateView):
    model = ServiceContact
    form_class = ServiceContactForm
    template_name = 'contacts/contact-create.html'
    success_url = reverse_lazy('contact-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ServiceContactDetailView(LoginRequiredMixin, views.DetailView):
    model = ServiceContact
    template_name = 'contacts/contact-detail.html'
    context_object_name = 'contact'

    def get_queryset(self):
        return ServiceContact.objects.filter(owner=self.request.user)


class ServiceContactUpdateView(LoginRequiredMixin, views.UpdateView):
    model = ServiceContact
    form_class = ServiceContactForm
    template_name = 'contacts/contact-edit.html'

    def get_queryset(self):
        return ServiceContact.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('contact-detail', kwargs={'pk': self.object.pk})


class ServiceContactDeleteView(LoginRequiredMixin, views.DeleteView):
    model = ServiceContact
    template_name = 'contacts/contact-delete.html'
    success_url = reverse_lazy('contact-list')

    def get_queryset(self):
        return ServiceContact.objects.filter(owner=self.request.user)