from django.contrib import admin
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('api/v1/auth/', include('api.v1.authusercheck.urls', namespace="auth_check")),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),
    path('admin/', admin.site.urls),
]
