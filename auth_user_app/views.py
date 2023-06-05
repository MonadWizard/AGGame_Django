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
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.http import Http404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db import connection
import json

from .models import User
from .utils import Util,image_decoder, get_all_images_name, remove_list_of_images
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

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from rest_framework_simplejwt.authentication import JWTAuthentication



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

        return Response(data, status=status.HTTP_200_OK)


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
        token = serializer.validated_data['refresh']

        try:
            RefreshToken(token).blacklist()
        except (TokenError, InvalidToken):
            pass

        # Invalidate the access token
        access_token = request.auth
        if access_token is not None:
            try:
                OutstandingToken.objects.filter(token=access_token).delete()
            except TokenError:
                pass

        return Response({'message': 'User successfully logged out.'}, status=status.HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET','POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def edit_user_profile(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':

        req_data = request.data
        if 'user_photopath' in req_data:
            base64_images = request.data['user_photopath']
            # image_extension = request.data['user_photopath_extension']
            userid = request.data['userid']
            MEDIA_ROOT = settings.MEDIA_ROOT
            prifile_picture_path = '/profilepic/' + str(userid) + '/'
            path = MEDIA_ROOT + prifile_picture_path 

            data = json.dumps(req_data)
            data = json.loads(data)
            # handle base64_images is empty or not
            try:
                for image_extension, base64_image in base64_images.items():
                    # take last part from splitted image_extension
                    image_decoder(base64_image, image_extension.rsplit('_',1)[-1], userid,path)
                    # image_urls = image_urls + [image_url]
                    # data['user_photopath'] = image_urls
                    # data['user_photopath'] = path
                    data['user_photopath'] = prifile_picture_path
            except:
                pass
        
        data = json.dumps(data)

        query = f"select edit_profile('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                return Response(
                    {
                        "status": "success",
                        "data": "profile updated",
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
def update_playing_sports(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        # initial ['player_image']
        data = json.dumps(request.data)
        data = json.loads(data)

        userid = request.data['userid']
        MEDIA_ROOT = settings.MEDIA_ROOT
        playingsports_picture_path = '/playingsports/' + str(userid) + '/'
        path = MEDIA_ROOT + playingsports_picture_path

        if 'player_image' in request.data['user_playing_sports'][0]:
            base64_images = request.data['user_playing_sports'][0]['player_image']
            # image_extension = request.data['user_photopath_extension']

            # handle base64_images is empty or not
            try:
                for image_extension, base64_image in base64_images.items():
                    # take last part from splitted image_extension
                    image_decoder(base64_image, image_extension.rsplit('_',1)[-1], userid,path)
                    # image_urls = image_urls + [image_url]
                    # data['user_photopath'] = image_urls
                    # data['user_photopath'] = path
            except:
                pass
            # data['user_photopath'] = image_urls
        data['user_playing_sports'][0]['player_image'] = playingsports_picture_path
        

        data = json.dumps(data)
        # print('data::::::::::::',data)
        
        # query = f"select edit_profile_interested_sports('{data}'::jsonb);"
        query = f"select edit_profile_playing_sports('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
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
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
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

            






# get all image url from file location


@api_view(['GET','POST'])
def get_image(request, table_name,user_id):

    if request.method =='GET':
        userid = user_id
        tablename = table_name
        query = f"select image_path('{tablename}','{userid}');"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchone()[0]
                try:
                    row = cursor.fetchone()[0]
                    images = get_all_images_name(row)
                except:
                    images = []
                return Response(
                    {
                        "status": "success",
                        "data": images,
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




@api_view(['GET','POST'])
def get_playing_sports(request, sports_name,user_id):

    if request.method =='GET':
        user_id = user_id
        sports_name = sports_name
        query = f"select get_playing_sports_data('{sports_name}','{user_id}');"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
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





@api_view(['GET','POST'])
def check_callphone(request, user_callphone):

    if request.method =='GET':
        data = user_callphone
        query = f"select check_callphone_existence('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
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





@api_view(['GET','POST'])
def check_mail(request, user_mail):

    if request.method =='GET':
        data = user_mail
        query = f"select check_email_existence('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
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




@api_view(['GET','POST'])
def check_username(request, username):

    if request.method =='GET':
        data = username
        query = f"select check_username_existence('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
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





@api_view(['GET','POST'])
def delete_listof_carrer_highlight(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        query = f"select delete_listof_carrer_highlight('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                return Response(
                    {
                        "status": "success",
                        "data": "successfully remove data from carrer highlight",
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
def delete_listof_image(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        user_id = request.data['user_id']
        where = request.data['where']
        images = request.data['images']
        query = f"select image_path('{where}','{user_id}');"
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    path = cursor.fetchone()[0]
                    remove_list_of_images(path, images)
                    images = 'removing successfully image' 
                except:
                    images = 'faied successfully removing image'
                return Response(
                    {
                        "status": "success",
                        "data": images,
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



