from django.urls import include, path

from .views import (
    ObtainAuthTokenView
)

app_name = "user"

urlpatterns = [
    path("login/", ObtainAuthTokenView.as_view()),
    
]
