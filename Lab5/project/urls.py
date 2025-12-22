from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="app/password_reset_form.html",
                                              email_template_name="app/password_reset_email.html"),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),
         name='password_reset_complete'),
]