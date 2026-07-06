from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "phone",
            "address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Age must be greater than 0."
            )
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits."
            )

        return value