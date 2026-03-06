from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from TailTales.care.forms import AppointmentForm, PreventiveCareForm
from TailTales.care.models import Appointment, PreventiveCare


# -------- Appointments --------

class AppointmentListView(LoginRequiredMixin, views.ListView):
    model = Appointment
    template_name = 'care/appointment-list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user).order_by('date')


class AppointmentCreateView(LoginRequiredMixin, views.CreateView):
    model = Appointment
    template_name = 'care/appointment-create.html'
    success_url = reverse_lazy('appointment-list')

    def get_form_class(self):
        return AppointmentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AppointmentDetailView(LoginRequiredMixin, views.DetailView):
    model = Appointment
    template_name = 'care/appointment-detail.html'
    context_object_name = 'appointment'

    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user)


class AppointmentUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Appointment
    template_name = 'care/appointment-edit.html'

    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user)

    def get_form_class(self):
        return AppointmentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('appointment-detail', kwargs={'pk': self.object.pk})


class AppointmentDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Appointment
    template_name = 'care/appointment-delete.html'
    success_url = reverse_lazy('appointment-list')

    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user)


# -------- Preventive Care --------

class PreventiveCareListView(LoginRequiredMixin, views.ListView):
    model = PreventiveCare
    template_name = 'care/preventivecare-list.html'
    context_object_name = 'care_items'

    def get_queryset(self):
        return PreventiveCare.objects.filter(pet__owner=self.request.user).order_by('next_due_date')


class PreventiveCareCreateView(LoginRequiredMixin, views.CreateView):
    model = PreventiveCare
    template_name = 'care/preventivecare-create.html'
    success_url = reverse_lazy('preventivecare-list')

    def get_form_class(self):
        return PreventiveCareForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PreventiveCareDetailView(LoginRequiredMixin, views.DetailView):
    model = PreventiveCare
    template_name = 'care/preventivecare-detail.html'
    context_object_name = 'care_item'

    def get_queryset(self):
        return PreventiveCare.objects.filter(pet__owner=self.request.user)


class PreventiveCareUpdateView(LoginRequiredMixin, views.UpdateView):
    model = PreventiveCare
    template_name = 'care/preventivecare-edit.html'

    def get_queryset(self):
        return PreventiveCare.objects.filter(pet__owner=self.request.user)

    def get_form_class(self):
        return PreventiveCareForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('preventivecare-detail', kwargs={'pk': self.object.pk})


class PreventiveCareDeleteView(LoginRequiredMixin, views.DeleteView):
    model = PreventiveCare
    template_name = 'care/preventivecare-delete.html'
    success_url = reverse_lazy('preventivecare-list')

    def get_queryset(self):
        return PreventiveCare.objects.filter(pet__owner=self.request.user)