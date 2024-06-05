from django.urls import path, re_path, include
from .views import profile_view, home_view
from allauth.account.views import (LoginView, LogoutView, SignupView,
                                   PasswordChangeView, PasswordSetView,
                                   PasswordResetView, PasswordResetDoneView,
                                   PasswordResetFromKeyView, PasswordResetFromKeyDoneView,
                                   EmailVerificationSentView, ConfirmEmailView, EmailView,)
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                                PasswordResetView, PasswordResetConfirmView,)

app_name = 'customer'

# urlpatterns = [
#     # Вход
#     path('accounts/login/', LoginView.as_view(), name='account_login'),
#
#     # Выход
#     path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
#
#     # Регистрация
#     path('accounts/signup/', SignupView.as_view(), name='account_signup'),
#
#     # Смена пароля
#     path('accounts/password/change/', PasswordChangeView.as_view(), name='account_change_password'),
#
#     # Установка пароля
#     path('accounts/password/set/', PasswordSetView.as_view(), name='account_set_password'),
#
#     # Сброс пароля
#     path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
#     path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='account_reset_password_done'),
#     re_path(r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', PasswordResetFromKeyView.as_view(),
#             name='account_reset_password_from_key'),
#     path('accounts/password/reset/key/done/', PasswordResetFromKeyDoneView.as_view(),
#          name='account_reset_password_from_key_done'),
#
#     # Подтверждение адреса электронной почты
#     path('accounts/email/', EmailView.as_view(), name='account_email'),
#     path('accounts/confirm-email/', EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
#     path('accounts/confirm-email/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
#
#     path('profile/', profile_view, name='profile'),
#     path('', home_view, name='home'),
# ]


urlpatterns = [
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/rest-auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/rest-auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('api/rest-auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/rest-auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
]
