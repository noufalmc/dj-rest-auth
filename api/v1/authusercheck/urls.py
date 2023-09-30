from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView


app_name = "authusercheck"
urlpatterns = [

    path('register/', RegisterView.as_view(), name="register"),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('login/', LoginView.as_view(), name=""),
    path('logout/', LogoutView.as_view()),

]
