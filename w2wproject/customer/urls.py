from django.urls import path
from allauth.account.views import SignupView, LoginView
from .views import send_test_email

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(template_name='registration/signup.html'), name='account_signup'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='account_login'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]
