from django.urls import path
app_name = 'bankai'
from .views import hello

urlpatterns = [
    path('bankai/', hello),
]