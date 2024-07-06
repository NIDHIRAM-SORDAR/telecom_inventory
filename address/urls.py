from django.urls import path
from .views import test_bootstrap

urlpatterns = [
    path('test-bootstrap/', test_bootstrap, name='test_bootstrap'),
]
