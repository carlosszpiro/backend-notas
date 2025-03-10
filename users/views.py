from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from users.models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer


class CustomUserRegisterView(generics.CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer
  permission_classes = [AllowAny,]


class ChangePasswordView(generics.UpdateAPIView):
  serializer_class = ChangePasswordSerializer
  model = CustomUser
  permission_classes = [IsAuthenticated,]

  def get_object(self):
    return self.request.user

  def update(self, request, *args, **kwargs):
    serializer = self.get_serializer(
        data=request.data, context={"request": request}
    )

    serializer.is_valid(raise_exception=True)

    user = self.get_object()
    serializer.update(user, serializer.validated_data)

    return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
