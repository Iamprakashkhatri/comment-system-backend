from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email", "first_name","last_name")

class UserAuthTokenSerializer(AuthTokenSerializer):
    username = serializers.CharField(label=_("Username"), write_only=True, required=False)
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}, trim_whitespace=False, write_only=True, required=False
    )
    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(request=self.context.get("request"), username=username, password=password)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True,required=True)
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email","password","confirm_password")
        

    def validate(self, attrs):

        if attrs['password'] != attrs['confirm_password']:
                raise serializers.ValidationError('Passwords Did Not Match')
        # attrs['user']=attrs
        return attrs
