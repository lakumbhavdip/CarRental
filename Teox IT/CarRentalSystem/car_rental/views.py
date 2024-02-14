from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Admin
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
# Create your views here.



class AdminRegistrationAPIView(APIView):
    def post(self, request):
        # Retrieve parameters from request body
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if company_name and email_address are provided
        if not full_name:
            return Response({'status': 400, 'message': 'Full name is required'}, status=status.HTTP_200_OK)
        
        if not email:
            return Response({'status': 400, 'message': 'Email is required'}, status=status.HTTP_200_OK)
        
        if not password:
            return Response({'status': 400, 'message': 'password is required'}, status=status.HTTP_200_OK)

        try:
            print(full_name,email,password)
            # Check if a record with the same company name or email address already exists
            existing_record = Admin.objects.filter(email=email).first()
            if existing_record:
                return Response({'status': 400, 'message': 'A record with the same email address already exists.'}, status=status.HTTP_200_OK)
            
            hashed_password = make_password(password)
            print(hashed_password)
            user = Admin.objects.create(
                full_name=full_name,
                email=email,
                password=hashed_password,
                created_at=datetime.now()
            )
            print(user)
            user.save()

            response_data = {
                'status': 200,
                'message': 'Registration successful.',
                'email': email,
                'password': password
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 400, 'message': 'Email address is already registered.'}, status=status.HTTP_200_OK)



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
        
        return Response({
            'status': '200',
            'message': 'Login successful.',
        },status=status.HTTP_200_OK)

