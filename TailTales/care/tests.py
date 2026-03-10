from datetime import timedelta
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from TailTales.care.forms import AppointmentForm, PreventiveCareForm
from TailTales.care.models import Appointment, PreventiveCare
from TailTales.contacts.models import ServiceContact
from TailTales.pets.models import Pet


class CareBaseTestMixin:
    def setUp(self):
        self.user = User.objects.create_user(
            username='ana',
            password='pass12345',
            email='ana@example.com',
        )
        self.other_user = User.objects.create_user(
            username='other',
            password='pass12345',
            email='other@example.com',
        )

        self.pet = Pet.objects.create(
            owner=self.user,
            name='Rita',
            species='Dog',
            breed='Husky',
            age=3,
            weight=20.5,
        )
        self.other_pet = Pet.objects.create(
            owner=self.other_user,
            name='Lee',
            species='Dog',
            breed='German Shepherd',
            age=4,
            weight=30.0,
        )

        self.contact = ServiceContact.objects.create(
            owner=self.user,
            contact_type='Vet',
            name='Happy Vet',
            phone='+441234567890',
            email='vet@example.com',
        )
        self.other_contact = ServiceContact.objects.create(
            owner=self.other_user,
            contact_type='Vet',
            name='Other Vet',
            phone='+441111111111',
            email='other-vet@example.com',
        )


class PreventiveCareModelTests(CareBaseTestMixin, TestCase):
    def test_save_sets_next_due_date(self):
        given_date = timezone.localdate() - timedelta(days=10)

        care_item = PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=given_date,
        )

        self.assertEqual(care_item.next_due_date, given_date + timedelta(days=30))

    def test_status_returns_upcoming(self):
        care_item = PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=timezone.localdate(),
        )

        self.assertEqual(care_item.status, 'Upcoming')

    def test_status_returns_due_today(self):
        care_item = PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=timezone.localdate() - timedelta(days=30),
        )

        self.assertEqual(care_item.status, 'Due today')

    def test_status_returns_overdue(self):
        care_item = PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=timezone.localdate() - timedelta(days=40),
        )

        self.assertEqual(care_item.status, 'Overdue')

    def test_unique_constraint_allows_only_one_care_type_per_pet(self):
        PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=timezone.localdate() - timedelta(days=5),
        )

        duplicate = PreventiveCare(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Another Product',
            interval_days=90,
            last_given_date=timezone.localdate() - timedelta(days=5),
        )

        with self.assertRaises(IntegrityError):
            duplicate.save()


class AppointmentModelValidationTests(CareBaseTestMixin, TestCase):
    def test_appointment_date_cannot_be_in_the_past(self):
        appointment = Appointment(
            pet=self.pet,
            service_contact=self.contact,
            title='Annual check',
            date=timezone.localdate() - timedelta(days=1),
        )

        with self.assertRaises(ValidationError):
            appointment.full_clean()


class FormTests(CareBaseTestMixin, TestCase):
    def test_appointment_form_filters_pets_by_user(self):
        form = AppointmentForm(user=self.user)

        self.assertIn(self.pet, form.fields['pet'].queryset)
        self.assertNotIn(self.other_pet, form.fields['pet'].queryset)

    def test_appointment_form_filters_service_contacts_by_user(self):
        form = AppointmentForm(user=self.user)

        self.assertIn(self.contact, form.fields['service_contact'].queryset)
        self.assertNotIn(self.other_contact, form.fields['service_contact'].queryset)

    def test_preventive_care_form_filters_pets_by_user(self):
        form = PreventiveCareForm(user=self.user)

        self.assertIn(self.pet, form.fields['pet'].queryset)
        self.assertNotIn(self.other_pet, form.fields['pet'].queryset)


class CareViewTests(CareBaseTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.appointment = Appointment.objects.create(
            pet=self.pet,
            service_contact=self.contact,
            title='Vaccination',
            date=timezone.localdate() + timedelta(days=2),
        )
        self.other_appointment = Appointment.objects.create(
            pet=self.other_pet,
            service_contact=self.other_contact,
            title='Other appointment',
            date=timezone.localdate() + timedelta(days=3),
        )
        self.care_item = PreventiveCare.objects.create(
            pet=self.pet,
            care_type='flea_tick',
            product_name='Frontline',
            interval_days=30,
            last_given_date=timezone.localdate() - timedelta(days=10),
        )
        self.other_care_item = PreventiveCare.objects.create(
            pet=self.other_pet,
            care_type='deworming',
            product_name='Drontal',
            interval_days=90,
            last_given_date=timezone.localdate() - timedelta(days=20),
        )

    def test_appointment_list_requires_login(self):
        response = self.client.get(reverse('appointment-list'))
        self.assertEqual(response.status_code, 302)

    def test_appointment_detail_allows_owner(self):
        self.client.login(username='ana', password='pass12345')
        response = self.client.get(
            reverse('appointment-detail', kwargs={'pk': self.appointment.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_appointment_detail_blocks_non_owner(self):
        self.client.login(username='ana', password='pass12345')
        response = self.client.get(
            reverse('appointment-detail', kwargs={'pk': self.other_appointment.pk})
        )

        self.assertEqual(response.status_code, 404)

    def test_preventive_care_detail_blocks_non_owner(self):
        self.client.login(username='ana', password='pass12345')
        response = self.client.get(
            reverse('preventivecare-detail', kwargs={'pk': self.other_care_item.pk})
        )

        self.assertEqual(response.status_code, 404)

    def test_mark_given_blocks_non_owner(self):
        self.client.login(username='ana', password='pass12345')

        response = self.client.post(
            reverse('preventivecare-mark-given', kwargs={'pk': self.other_care_item.pk}),
            data={
                'given_date': timezone.localdate(),
                'notes': 'Sneaky goblin attempt',
            },
        )

        self.assertEqual(response.status_code, 404)