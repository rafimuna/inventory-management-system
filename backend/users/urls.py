from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, DashboardView, VerifyEmailView

urlpatterns = [
    
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/dashboard/", DashboardView.as_view(), name="dashboard"),
    path("api/verify-email/", VerifyEmailView.as_view(), name="verify-email"),
]
