from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'User', Index,basename="user")

urlpatterns = [
    path('',include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest')),
    path('getpairtoken/',TokenObtainPairView.as_view(),name='getpairtoken'),
    path('getaccestoken/',TokenRefreshView.as_view(),name='getaccestoken'),
    path('tokenverification',TokenVerifyView.as_view(),name='tokenverification')
]