from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('signup/', Patient_Signup.as_view(),name='signup'),
    path('signin', MyTokenObtainPairView.as_view()),
    path('signin/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signout', LogoutView.as_view(), name='auth_logout'),
    path('appointment', BookAppointment.as_view(), name='appointment'),


]
