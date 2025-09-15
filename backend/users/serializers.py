from rest_framework import serializers
from .models import CustomUser
from .tasks import send_verification_email  # Celery task
from django.utils.crypto import get_random_string

# Token generator
def generate_email_token():
    return get_random_string(50)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        # 1️⃣ Create user as inactive
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=False  # inactive until email verified
        )

        # 2️⃣ Generate email verification token
        token = generate_email_token()
        user.email_verification_token = token
        user.save()

        # 3️⃣ Trigger Celery task to send verification email
        send_verification_email.delay(user.email, token)

        return user
