from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from TailTales.care.validators import (
    validate_future_or_today_date,
    validate_today_or_past_date,
)
from TailTales.contacts.models import ServiceContact
from TailTales.pets.models import Pet
from datetime import timedelta


class Appointment(models.Model):
    TITLE_MIN_LENGTH = 2
    TITLE_MAX_LENGTH = 50

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='appointments',
    )

    service_contact = models.ForeignKey(
        ServiceContact,
        on_delete=models.SET_NULL,
        related_name='appointments',
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(
                TITLE_MIN_LENGTH,
                message='Appointment title must be at least 2 characters long.',
            ),
        ],
    )

    date = models.DateField(
        validators=[validate_future_or_today_date],
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.title} - {self.pet.name}'




class PreventiveCare(models.Model):

    PRODUCT_NAME_MIN_LENGTH = 2
    PRODUCT_NAME_MAX_LENGTH = 50

    CARE_TYPE_CHOICES = [
        ('flea_tick', 'Flea & Tick'),
        ('deworming', 'Deworming'),
        ('heartworm', 'Heartworm'),
        ('other', 'Other'),
    ]

    INTERVAL_CHOICES = [
        (30, 'Monthly (30 days)'),
        (90, 'Every 3 months'),
        (180, 'Every 6 months'),
        (365, 'Yearly'),
    ]

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='preventive_care_items',
    )

    care_type = models.CharField(
        max_length=20,
        choices=CARE_TYPE_CHOICES,
    )

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(
                PRODUCT_NAME_MIN_LENGTH,
                message='Product name must be at least 2 characters long.',
            ),
        ],
    )

    interval_days = models.PositiveIntegerField(
        choices=INTERVAL_CHOICES,
        default=30,
        help_text="How often this treatment should repeat.",
    )

    last_given_date = models.DateField(
        validators=[validate_today_or_past_date],
    )

    next_due_date = models.DateField(
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    def record_dose(self, given_date, notes=''):
        PreventiveCareDose.objects.create(
            preventive_care=self,
            given_date=given_date,
            notes=notes,
        )
        self.last_given_date = given_date
        self.next_due_date = given_date + timedelta(days=self.interval_days)
        self.save()

    @property
    def status(self):
        if not self.next_due_date:
            return 'Unknown'

        today = timezone.localdate()
        if self.next_due_date < today:
            return 'Overdue'
        if self.next_due_date == today:
            return 'Due today'
        return 'Upcoming'

    @property
    def overdue_days(self):
        if not self.next_due_date:
            return 0

        days = (timezone.localdate() - self.next_due_date).days
        return days if days > 0 else 0

    def save(self, *args, **kwargs):
        if self.last_given_date and self.interval_days:
            self.next_due_date = self.last_given_date + timedelta(days=self.interval_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_care_type_display()} - {self.pet.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pet', 'care_type'],
                name='unique_preventive_care_type_per_pet',
            ),
        ]

class PreventiveCareDose(models.Model):

    preventive_care = models.ForeignKey(
        PreventiveCare,
        on_delete=models.CASCADE,
        related_name='doses',
    )

    given_date = models.DateField(
        validators=[validate_today_or_past_date],
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-given_date']

    def __str__(self):
        return f'{self.preventive_care} dose on {self.given_date}'