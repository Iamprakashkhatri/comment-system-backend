from django.urls import include, path
from .routers import router

from .views import *

app_name = "comment"

urlpatterns = [
    path('', include(router.urls)),
]
