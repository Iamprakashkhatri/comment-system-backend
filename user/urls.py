from django.urls import include, path

from .views import (
    ObtainAuthTokenView,
    RegisterUserAPIView
)

app_name = "user"

urlpatterns = [
    path("login/", ObtainAuthTokenView.as_view()),
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    
]
