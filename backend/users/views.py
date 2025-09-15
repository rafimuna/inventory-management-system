from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        cache_key = f"dashboard_{user_id}"

        data = cache.get(cache_key)
        if not data:
            data = {"message": f"Welcome {request.user.email}"}
            cache.set(cache_key, data, timeout=60)

        return Response(data)

class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get("token")
        try:
            user = CustomUser.objects.get(email_verification_token=token)
            user.is_active = True
            user.email_verification_token = ""
            user.save()
            return Response({"message": "Email verified successfully"})
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid token"}, status=400)
