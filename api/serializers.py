from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Items, Receipt


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name', 'email', 'password','phonenumber','groups']
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


class CreateCashier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','full_name','password','email','phone_number','groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return  user


class CreateItem(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = '__all__'

    def create(self, validated_data):
        user = Items.objects.create(**validated_data)
        user.save()

        return  user

class CreateReceipt(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = '__all__'

    def create(self, validated_data):
        user = Receipt.objects.create(**validated_data)
        user.save()

        return  user

#ToDo

#Add later on Serializer for creating another Admin... Admin to create a General Manager         
    

