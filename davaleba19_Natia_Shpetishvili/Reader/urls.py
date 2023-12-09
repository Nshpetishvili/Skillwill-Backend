from django.urls import path
from .views import reader_profile

urlpatterns = [
    path('profile/', reader_profile, name='reader_profile'),
]
