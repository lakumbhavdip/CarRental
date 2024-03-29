from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Admin, Car, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from rest_framework.authtoken.models import Token
from .serializers import car_Serializer
# Create your views here.



class AdminRegistrationAPIView(APIView):
    def post(self, request):
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not full_name or not email or not password:
            return Response({'status': 400, 'message': 'Full name, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            existing_record = Admin.objects.filter(email=email).first()
            if existing_record:
                return Response({'status': 400, 'message': 'A record with the same email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash the password
            hashed_password = make_password(password)

            user = Admin.objects.create(
                full_name=full_name,
                email=email,
                password=hashed_password,
            )

            response_data = {
                'status': 201,  
                'message': 'Registration successful.',
                'email': email,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
#login APIView 
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email:
            return Response({'status':400,'message': 'Email address is required.'},status=status.HTTP_200_OK)
        
        if not password:
            return Response({'status': 400,'message': 'Password is required.'})

        try:
            admin_data = Admin.objects.get(email=email)
        except Admin.DoesNotExist:
            return Response({'status':400,'message': 'User not found.'},status=status.HTTP_200_OK)

        if not check_password(password, admin_data.password):
            return Response({'status': 400,'message': 'Incorrect password.'},status=status.HTTP_200_OK)
        try:
            check_email_pswd = Admin.objects.get(email=email,password=password)
            if check_email_pswd:
                request.session['userid'] = check_email_pswd.id
        except Admin.DoesNotExist:
            return Response({'status':400,'message': 'Password or Email Wrong.'},status=status.HTTP_200_OK)
        return Response({
            'status': '200',
            'message': 'Login successful.',
        },status=status.HTTP_200_OK)
        
class LogOutAPIView(APIView):
    def logout(request):
        del request.session['userid']
        response_data = {
            'status': 201,  
            'message': 'Log Out successful.',
        }
        return Response(response_data, status=status.HTTP_201_CREATED)



class CustomerRegistrationAPIView(APIView):
    def post(self, request):
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        address = request.data.get('address')
        password = request.data.get('password')

        if not full_name or not email or not password:
            return Response({'status': 400, 'message': 'Full name, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            existing_record = Customer.objects.filter(email=email).first()
            if existing_record:
                return Response({'status': 400, 'message': 'A record with the same email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash the password
            hashed_password = make_password(password)

            user = Customer.objects.create(
                full_name=full_name,
                email=email,
                password=hashed_password,
                phone=phone,
                address=address,
                created_at=timezone.now(),
            )

            response_data = {
                'status': 201,  
                'message': 'Registration successful.',
                'email': email,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
#login APIView 
class CustomerLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email:
            return Response({'status':400,'message': 'Email address is required.'},status=status.HTTP_200_OK)
        
        if not password:
            return Response({'status': 400,'message': 'Password is required.'})

        try:
            admin_data = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({'status':400,'message': 'User not found.'},status=status.HTTP_200_OK)

        if not check_password(password, admin_data.password):
            return Response({'status': 400,'message': 'Incorrect password.'},status=status.HTTP_200_OK)
        
        return Response({
            'status': '200',
            'message': 'Login successful.',
        },status=status.HTTP_200_OK)


class CustomerUpdateAPIView(APIView):
    def put(self, request):
        
        customer_id = request.data.get('id')
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        address = request.data.get('address')

        if not customer_id:
            return Response({'status': 400, 'message': 'Customer id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({'status':400,'message': 'User not found.'},status=status.HTTP_200_OK)

        try:
            existing_record = Customer.objects.filter(email=email).first()
            if existing_record:
                return Response({'status': 400, 'message': 'A record with the same email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            if full_name:
                customer.full_name = full_name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone
            if address:
                customer.address = address

            # Save the updated customer object
            customer.save()
          
          
            response_data = {
                'status': 201,  
                'message': 'Updated successful.',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        


class VehicalmanageAPIView(APIView):
    def post(self, request):
        brand = request.data.get('brand')
        model = request.data.get('model')
        year = request.data.get('year')
        registration_number = request.data.get('registration_number')

        if not brand or not model or not year or not registration_number:
            return Response({'status': 400, 'message': 'brand ,model, year, and registration_number are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            car = Car.objects.create(
                brand=brand,
                model=model,
                year=year,
                registration_number=registration_number,
            )

            response_data = {
                'status': 201,  
                'message': 'Registration successful.',
                'brand':brand,
                'model':model,
                'year':year,
                'registration_number':registration_number
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCustomerAPIView(APIView):
    def delete(self, request):
        
        customer_id = request.data.get('id')
      
        if not customer_id:
            return Response({'status': 400, 'message': 'Customer id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({'status':400,'message': 'User not found.'},status=status.HTTP_200_OK)

        try:
            if customer_id:
                customer.is_deleted = True

            customer.save()
          
            response_data = {
                'status': 201,  
                'message': 'Deleted successful.',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class PasswordChangeAPIView(APIView):
    def put(self, request):
        
        admin_id = request.data.get('id')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not admin_id:
            return Response({'status': 400, 'message': 'Admin id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            admin_data = Admin.objects.get(id=admin_id,email=email)
        except Customer.DoesNotExist:
            return Response({'status':400,'message': 'User not found.'},status=status.HTTP_200_OK)
        try:
            if password:
                admin_data.password = password
            
            admin_data.save()
          
          
            response_data = {
                'status': 201,  
                'message': 'Password Changed successful.',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CarDetailsAPIView(APIView):
    def get(self, request):
        car_details = Car.objects.all()
            
        car_serializer = car_Serializer(car_details, many=True)
        car_data = car_serializer.data
 
        response_data = {
                'status': 201,  
                'message': 'Log Out successful.',
                'car-details':car_data
            }
        return Response(response_data, status=status.HTTP_201_CREATED)



