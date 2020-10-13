from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

app_name = "account"  #new added line after changing myside/url.py path from commentted to new
urlpatterns = [
    #path('login/', views.user_login,name='user_login'),
    path('login/',LoginView.as_view(template_name='account/login2.html'),name='user_login'),
    path('logout/',LogoutView.as_view(template_name='account/logout.html'),name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', PasswordChangeView.as_view(template_name="account/password_change_form.html",success_url="/account/password-change-done/"),name='password_hcange'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name='password_change_done'),
    path('password-reset/',PasswordResetView.as_view(template_name="account/password_reset_form.html",email_template_name="account/password_reset_email.html",
                           success_url='/account/password-reset-done/'),name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",success_url="/account/password-reset-complete/"),name="password_reset_confirm"),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),name='password_reset_complete'),
    path('my-information/',views.myself,name="my_information"),
    path('edit-my-information/', views.myself_edit,name="edit_my_information"),
]