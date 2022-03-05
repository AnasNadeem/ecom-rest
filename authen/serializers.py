from django.contrib.auth.models import User
from authen.models import Account, AccountAddress
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=4, write_only=True)
    class Meta:
        model = User
        fields=(
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            
        )

    def validate(self, attrs):
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('Username should contain alphanumeric characters only')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    
    
class LoginSerializer(serializers.ModelSerializer):
    is_verified = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('username','is_active','is_verified')

    def get_is_verified(self, obj):
        user = User.objects.get(username=obj.username)
        return Account.objects.get(user=user).is_verified

class AccountAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAddress
        fields = '__all__'
