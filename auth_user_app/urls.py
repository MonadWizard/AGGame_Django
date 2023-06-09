from django.urls import path
from .views import  (SignUpMailVerifyRequestView,
                    VerifyEmailCOmpleteSignUpView,
                    UpdateRegisterView,
                    LogoutAPIView,
                    SetNewPasswordAPIView,
                    LoginAPIView,
                    PasswordTokenCheckAPI,
                    RequestPasswordResetEmail,
                    ViewUser)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('signup-request/', SignUpMailVerifyRequestView.as_view(), name='signup-request'),
    path('signup-email-verify/', VerifyEmailCOmpleteSignUpView.as_view(), name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    
    path('Update-register/<str:user_email>', UpdateRegisterView.as_view(), name="update-register"),

    path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),name='password-reset-complete'),
    path('user/<str:pk>', ViewUser.as_view(), name="user-data"),
]