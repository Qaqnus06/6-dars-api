from rest_framework  import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    password = serializers.CharField(min_length=4)


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, min_length=4, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=20,required=True)
    confirm_password=serializers.CharField(max_length=20,required=True)

class CodeVerificationSerializer(serializers.Serializer):
    email = serializers.CharField()
    code = serializers.CharField(max_length=6)
    