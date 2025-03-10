from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import CustomUserRegisterView, ChangePasswordView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("registro/", CustomUserRegisterView.as_view(), name="regitrar_user"),
    path("mudar-senha/", ChangePasswordView.as_view(), name="change_password")
]
