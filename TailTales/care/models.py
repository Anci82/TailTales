from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from TailTales.care.validators import (
    validate_future_or_today_date,
    validate_today_or_past_date,
)
from TailTales.contacts.models import ServiceContact
from TailTales.pets.models import Pet


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
        ('Flea and Tick', 'Flea and Tick'),
        ('Deworming', 'Deworming'),
        ('Heartworm', 'Heartworm'),
        ('Other', 'Other'),
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

    last_given_date = models.DateField(
        validators=[validate_today_or_past_date],
    )

    next_due_date = models.DateField(
        validators=[validate_future_or_today_date],
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    def clean(self):
        super().clean()

        if self.last_given_date and self.next_due_date:
            if self.next_due_date < self.last_given_date:
                raise ValidationError({
                    'next_due_date': 'Next due date cannot be earlier than the last given date.',
                })

    def __str__(self):
        return f'{self.care_type} - {self.pet.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pet', 'care_type'],
                name='unique_preventive_care_type_per_pet',
            ),
        ]