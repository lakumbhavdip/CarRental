from django.urls import path
from .views import AdminRegistrationAPIView, CustomerUYpdateAPIView,LoginAPIView,CustomerRegistrationAPIView,CustomerLoginAPIView

urlpatterns = [
    path('admin_register', AdminRegistrationAPIView.as_view(), name='admin_registrations'),
    path('admin_login', LoginAPIView.as_view(), name='admin_login'),
    path('customer_register', CustomerRegistrationAPIView.as_view(), name='customer_registrations'),
    path('customer_login', CustomerLoginAPIView.as_view(), name='customer_login'),
    path('customer_update', CustomerUYpdateAPIView.as_view(), name='customer_update'),
]