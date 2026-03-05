from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_future_or_today_date(value):
    if value < timezone.localdate():
        raise ValidationError('Appointment date cannot be in the past.')


def validate_today_or_past_date(value):
    if value > timezone.localdate():
        raise ValidationError('This date cannot be in the future.')