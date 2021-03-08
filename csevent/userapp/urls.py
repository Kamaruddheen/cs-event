from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # SignUp Form
    path('registration/', signup, name="signup"),
    # Events Register
    path('event_register/', event_register, name="event_register"),
    # 4 Events only 1 offline-mail
    path('event_register/ransack/', register_ransack, name="register_ransack"),
    path('event_register/codetreasure/', register_codetreasure,
         name="register_codetreasure"),
    path('event_register/impreza/', register_impreza, name="register_impreza"),
    path('event_register/webdodger/',
         register_webdodger, name="register_webdodger"),
]
