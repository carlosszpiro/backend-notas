from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ["email", "password", "password2",]

  def validate(self, data):
    if data["password"] != data["password"]:
      raise serializers.ValidationError(
          {"password2": "As senhas não coincidem"}
      )

    validate_password(data["password"])
    return data

  def create(self, validated_data):
    validated_data.pop("password2")
    user = CustomUser.objects.create_user(**validated_data)

    return user


class ChangePasswordSerializer(serializers.ModelSerializer):
  old_password = serializers.CharField(write_only=True, required=True)
  new_password = serializers.CharField(write_only=True, required=True)
  new_password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = CustomUser
    fields = ["old_password", "new_password", "new_password2",]

  def validate(self, data):
    if data['new_password'] != data['new_password2']:
      raise serializers.ValidationError(
          {"new_password2": "As senhas não coincidem."}
      )

    validate_password(data['new_password'])
    return data

  def validate_old_password(self, value):
    user = self.context["request"].user
    if not user.check_password(value):
      raise serializers.ValidationError(
          {"old_password": "A senha antiga está incorreta."}
      )

    return value

  def update(self, instance, validated_data):
    instance.set_password(validated_data["new_password"])
    instance.save()

    return instance
