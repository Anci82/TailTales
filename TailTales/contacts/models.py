from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from TailTales.contacts.validators import phone_number_validator


class ServiceContact(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 40
    PHONE_MAX_LENGTH = 15
    EMAIL_MAX_LENGTH = 100
    ADDRESS_MAX_LENGTH = 100

    TYPE_CHOICES = [
        ('Vet', 'Vet'),
        ('Groomer', 'Groomer'),
        ('Trainer', 'Trainer'),
        ('Other', 'Other'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='service_contacts',
    )

    contact_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(
                NAME_MIN_LENGTH,
                message='Contact name must be at least 2 characters long.',
            ),
        ],
    )

    phone = models.CharField(
        max_length=PHONE_MAX_LENGTH,
        validators=[phone_number_validator],
        blank=True,
        null=True,
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.name} - {self.contact_type}'