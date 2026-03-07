from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Pet(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 30
    BREED_MAX_LENGTH = 30
    PHOTO_URL_MAX_LENGTH = 500

    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pets',
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(
                NAME_MIN_LENGTH,
                message='Pet name must be at least 2 characters long.',
            ),
        ],
    )

    species = models.CharField(
        max_length=20,
        choices=SPECIES_CHOICES,
    )

    breed = models.CharField(
        max_length=BREED_MAX_LENGTH,
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.1)],
    )

    photo_url = models.URLField(
        max_length=PHOTO_URL_MAX_LENGTH,
        blank=True,
        null=True,
    )

    show_in_gallery = models.BooleanField(
        default=True,
        verbose_name='Show in public gallery',
    )

    def __str__(self):
        return f'{self.name} ({self.species})'