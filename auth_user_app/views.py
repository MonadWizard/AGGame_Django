from django.http import HttpResponse
from rest_framework import generics, status, views, permissions
from .serializers import (RegisterSerializer,
                        UpdateRegisterSerializer,
                        SetNewPasswordSerializer, 
                        ResetPasswordEmailRequestSerializer, 
                        EmailVerificationSerializer, 
                        LoginSerializer, 
                        LogoutSerializer, 
                        ViewUserSerializer )

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import permissions
from django.http import Http404

from rest_framework.decorators import api_view
from django.db import connection
import json

from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponsePermanentRedirect
import os
import datetime 



class SignUpMailVerifyRequestView(views.APIView):
    
    def post(self, request):
        data = request.data
        user_username = data['user_username']
        user_email = data['user_email']
        password = data['password']
        user_country = data['user_country']
        user_state_divition = data['user_state_divition']
        user_playing_city = data['user_playing_city']



# Token passing
        payload = {
            'user_email': user_email,
            'user_username': user_username,
            'password': password,
            'user_country': user_country,
            'user_state_divition': user_state_divition,
            'user_playing_city': user_playing_city,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30, seconds=00),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        
        email_body = 'Hi '+user_username + \
            ' Use the link below to verify your email \n ' + absurl
        
        data = {'email_body': email_body, 'to_email': user_email,
                'email_subject': 'Verify your email'}
        # print('data:', data)

        Util.send_email(data)

        return Response(data, status=status.HTTP_201_CREATED)


class VerifyEmailCOmpleteSignUpView(views.APIView):

    serializer_class = RegisterSerializer

    def get(self, request):
        token = request.GET.get('token')

        try:
            verified_mail_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # print("payload--------------",verified_mail_payload)


            # user = request.data
            # print('user',type(user))

            current_time = datetime.datetime.now() 
            current_time = current_time.strftime("%m%d%H%M%S%f")
            
            userid = current_time
            verified_mail_payload["userid"]= userid

            # print('user::::::::',user)

            serializer = self.serializer_class(data=verified_mail_payload)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            html = "<html><body>Verification Success. It's time for login</body></html>"
            return HttpResponse(html)
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            html = "<html><body>Activation Expired.</body></html>"
            return HttpResponse(html)
            # return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            html = "<html><body>Invalid token.</body></html>"
            return HttpResponse(html)
            # return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("successfully logout",status=status.HTTP_204_NO_CONTENT)



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET','POST'])
def edit_user_profile(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        query = f"select update_user_profile('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchone()
                # row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": "profile update success",
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )


@api_view(['GET','POST'])
def update_interested_sports(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        query = f"select profile_interested_sports('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchone()
                # row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": "row",
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            



@api_view(['GET','POST'])
def get_profile_info(request, user_id):

    if request.method =='GET':
        data = user_id
        query = f"select get_profile_info('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": row,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )


    elif request.method == 'POST':
        return Response('post data')

            


    























# no need to use this class................................................
class UpdateRegisterView(views.APIView):


    def get_object(self,user_email):
        try:
            return User.objects.get(user_email__exact=user_email)
        except User.DoesNotExist:
            raise Http404


    def put(self,request,user_email):
        user_email = self.get_object(user_email)
        fullname_pasport = request.data['user_username_passport']
        serializer = UpdateRegisterSerializer(user_email,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        # relativeLink = reverse('email-verify')
        email_body = 'Hi '+fullname_pasport + \
            ' welcome to probashi.. \n'
        data = {'email_body': email_body, 'to_email': user_email,
                'email_subject': 'welcome to probashi'}
        # print('data:::::::::', data)

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)
    


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        user_email = request.data.get('user_email', '')

        if User.objects.filter(user_email=user_email).exists():
            user = User.objects.get(user_email=user_email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.userid))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            # email_body = 'Hello, \n Use link below to reset your password  \n' + \
            #     absurl+"?redirect_url="+redirect_url
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl
            data = {'email_body': email_body, 'to_email': user.user_email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(userid=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error', 'Token is not valid, Please request a new link'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True, 'message': 'Credentials valid', 'uidb64': uidb64, 'token': token }, status=status.HTTP_200_OK)

            
        except DjangoUnicodeDecodeError as identifier:
            # try:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error', 'Token is not valid, Please request a new link'}, status=status.HTTP_400_BAD_REQUEST)
                    
            
class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class ViewUser(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_user(self,pk):
        try:
            return User.objects.get(userid=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk):

        user = self.get_user(pk)
        serializer = ViewUserSerializer(user)
        return Response (serializer.data)

    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = ViewUserSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



