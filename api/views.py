from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from .models import Items, Receipt, User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.authtoken.models import Token
from .permission import IsAdminOrCashier, IsAdminUser, IsLoggedInUserOrAdmin
from .serializers import CreateCashier, CreateItem, CreateReceipt
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from rest_framework.decorators import api_view


# Create your views here.

#create a pdf
# @api_view(['GET'])
# def receipt_pdf(request):
#     #Create ByteStream Buffer
#     buf =io.BytesIO()
    
#     #create canvas
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
#     #create text object
#     textobj = c.beginText()
#     textobj.setTexTOrigin(inch, inch)
#     textobj.setFont("Helvetica", 14)
    
#     #add content
#     lines = [
#         "This is line 1",
#         "This is line 3",
#         "This is line 4",
#     ]
#     #loop through lines
#     for line in lines:
#         textobj.textLine(line)
        
#     c.drawText(textobj)
#     c.showpage()
#     c.save()
#     buf.seek(0)
    
#     return FileResponse(buf, as_attachment=True, filename='test.pdf')
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'full_name': user.full_name,
            'group_id': user.groups_id,
            'email': user.email
        })
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):

        return CustomAuthToken().as_view()(request=request._request)

        # SEnd Response

    pass

class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
  
class StaffCreateViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateCashier
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
class ReceiptCreateViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = CreateReceipt
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminOrCashier]
        elif self.action == 'list':
            permission_classes = [IsAdminOrCashier]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminOrCashier]
        elif self.action == 'destroy':
            permission_classes = [IsAdminOrCashier]
        return [permission() for permission in permission_classes]
    
class ItemCreateViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = CreateItem
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]