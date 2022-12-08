from django.urls import re_path as url
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path(
        'signup/', views.SignUp.as_view(template_name='users/signup.html'),
        name='signup'),
    path(
        'login/',
        LoginView.as_view
        (template_name='users/login.html'),
        name='login'),
    path(
        'password_reset_form/',
        PasswordResetView.as_view
        (email_template_name='users/password_reset_email.html',template_name='users/password_reset_form.html',success_url='/users/password_reset/done/'),
        name='password_reset_form'),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view
        (template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    url(
        r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view
        (template_name='users/password_reset_confirm.html',success_url='/users/password_reset_complete/'),
        name='password_reset_confirm'),
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view
        (template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path(
        'password_change_form/',
        PasswordChangeView.as_view
        (template_name='users/password_change_form.html'),
        name='password_change'),
    path(
        'password_change_done/',
        PasswordChangeDoneView.as_view
        (template_name='users/password_change_done.html'),
        name='password_change_done'),
]
