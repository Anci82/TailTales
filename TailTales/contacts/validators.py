from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\+?\d+$',
    message='Phone number can contain only digits and an optional + at the beginning.',
)