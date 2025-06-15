from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/', register_user),
    path('public/', public_api, name='public_api'),
    path('protected/', protected_api, name='protected_api'),
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_view'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
]
