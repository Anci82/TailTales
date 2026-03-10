from rest_framework import serializers

from TailTales.care.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    service_contact_name = serializers.CharField(source='service_contact.name', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'title',
            'date',
            'notes',
            'is_completed',
            'pet',
            'pet_name',
            'service_contact',
            'service_contact_name',
        ]