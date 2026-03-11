from django.conf import settings
from django.core.mail import send_mail


def send_welcome_email(user):
    if not user.email:
        return

    send_mail(
        subject="Welcome to TailTales",
        message=(
            f"Hi {user.username},\n\n"
            "Welcome to TailTales.\n\n"
            "Your account is ready, and you can now start keeping track of your pets, care, and appointments."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )