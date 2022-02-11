from rest_framework import serializers
from django.contrib.auth import get_user_model


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name', 'email', 'password','groups']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }
    #Hash password function  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class Loginserializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
