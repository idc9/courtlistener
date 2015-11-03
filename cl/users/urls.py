from cl.users.forms import (
    CustomPasswordResetForm, CustomSetPasswordForm,
)
from cl.users import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Sign in/out and password pages
    url(r'^sign-in/$', auth_views.login, {
        'extra_context': {'private': False}},
        name="sign-in"),
    url(r'^sign-out/$', auth_views.logout, {'extra_context': {'private': False}}),
    url(r'^reset-password/$', auth_views.password_reset,
        {'extra_context': {'private': False},
         'password_reset_form': CustomPasswordResetForm}),
    url(r'^reset-password/instructions-sent/$', auth_views.password_reset_done,
        {'extra_context': {'private': False}}),
    url(r'^confirm-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect': '/reset-password/complete/',
         'set_password_form': CustomSetPasswordForm,
         'extra_context': {'private': False}}),
    url(r'^reset-password/complete/$', auth_views.login, {
        'template_name': 'registration/password_reset_complete.html',
        'extra_context': {'private': False}}),

    # Settings pages
    url(r'^profile/settings/$', views.view_settings, name='view_settings'),
    url(r'^profile/favorites/$', views.view_favorites),
    url(r'^profile/alerts/$', views.view_alerts),
    url(r'^profile/visualizations/$', views.view_visualizations,
        name='view_visualizations'),
    url(r'^profile/api/$', views.view_api, name='view_api'),
    url(r'^profile/password/change/$', views.password_change),
    url(r'^profile/delete/$', views.delete_account),
    url(r'^profile/delete/done/$', views.delete_profile_done),
    url(r'^register/$', views.register, name="register"),
    url(r'^register/success/$', views.register_success),

    # Registration pages
    url(r'^email/confirm/([0-9a-f]{40})/$', views.confirm_email),
    url(r'^email-confirmation/request/$', views.request_email_confirmation),
    url(r'^email-confirmation/success/$', views.email_confirm_success),
]