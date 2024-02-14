from django.urls import path
from .views import AdminRegistrationAPIView,LoginAPIView

urlpatterns = [
    path('admin_register', AdminRegistrationAPIView.as_view(), name='admin_registrations'),
    path('admin_login', LoginAPIView.as_view(), name='admin_login'),
]