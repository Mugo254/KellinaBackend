from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer, Loginserializer
from .models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt, datetime



# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        
        payload = {
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload,'secret', algorithm='HS256')
        
        response = Response({
            'jwt' : token
        })
        
        response.set_cookie(key='jwt', value = token, httponly=True)
        
        return response
        
            

    def get(self,request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token,'secret',algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user =User.objects.filter(id=payload['id']).first()
        serializer = RegisterSerializer(user)
        
        return Response(serializer.data)

class LogoutView(GenericAPIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'successfully Logged'
        }
        return response