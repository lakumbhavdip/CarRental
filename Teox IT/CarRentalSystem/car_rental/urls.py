from django.urls import path
from .views import AdminRegistrationAPIView, CustomerUpdateAPIView,LoginAPIView,CustomerRegistrationAPIView,CustomerLoginAPIView, VehicalmanageAPIView,DeleteCustomerAPIView,CarDetailsAPIView,LogOutAPIView

urlpatterns = [
    path('admin_register', AdminRegistrationAPIView.as_view(), name='admin_registrations'),
    path('admin_login', LoginAPIView.as_view(), name='admin_login'),
    path('customer_register', CustomerRegistrationAPIView.as_view(), name='customer_registrations'),
    path('customer_login', CustomerLoginAPIView.as_view(), name='customer_login'),
    path('customer_update', CustomerUpdateAPIView.as_view(), name='customer_update'),
    path('vehical_manage', VehicalmanageAPIView.as_view(), name='vehical_manage'),
    path('delete_customer', DeleteCustomerAPIView.as_view(), name='delete_customer'),
    path('car_details', CarDetailsAPIView.as_view(), name='car-details'),
    path('logout_admin', LogOutAPIView.as_view(), name='logout_admin'),
]