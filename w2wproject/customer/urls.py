from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from customer.views import CustomerViewSet, CustomConfirmEmailView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/registration/verify-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name="registration/email_confirm.html"), name='account_confirm_email'),
    re_path(r'account-confirm-email/(?P<key>[-:\w]+)/$', CustomConfirmEmailView.as_view(), name='custom_account_confirm_email'),
]

urlpatterns += [
    path('', RegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(r'account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name="registration/email_confirm.html"), name='account_confirm_email'),
]
