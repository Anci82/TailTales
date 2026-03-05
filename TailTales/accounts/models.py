from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    IMAGE_URL_MAX_LENGTH = 500

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    image_url = models.URLField(
        max_length=IMAGE_URL_MAX_LENGTH,
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username