from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from .views import LogoutView, LoginView, RegisterView

router = DefaultRouter()
router.register('staff', views.StaffCreateViewSet, basename='staff')
router.register('receipt', views.ReceiptCreateViewSet, basename='receipt')
router.register('item', views.ItemCreateViewSet, basename='item')


urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),

    path('logout', LogoutView.as_view()),
    
   
]