from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'),
    path('index', views.index, name="index"),
    path('tables/', views.tables, name="tables"),
    path('registrar_usuario/', views.registrar_usuario, name="registrar_usuario"),
    path('billing/', views.billing, name="billing"),
    path('virtual-reality/', views.virtual_reality, name="virtual_reality"),
    path('rtl/', views.rtl, name="rtl"),
    path('notifications/', views.notifications, name="notifications"),
    path('profile/', views.profile, name="profile"),
    path('map/', views.map, name="map"),
    path('icons/', views.icons, name="icons"),
    path('typography/', views.typography, name="typography"),
    path('template/', views.template, name="template"),
    path('productos/', views.productos, name="productos"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('clientes/', views.clientes, name="clientes"),
    path('registrar_clientes/', views.registrar_clientes, name="registrar_clientes"),
    path('charts/', views.charts, name="charts"),

    # Authentication
    path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
     path('logout/', views.user_logout_view, name='logout'),
    # path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='pages/password_change_done.html'
    # ), name="password_change_done" ),
    # path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    # path('accounts/password-reset-confirm/<uidb64>/<token>/', 
    #     views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='pages/password_reset_done.html'
    # ), name='password_reset_done'),
    # path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='pages/password_reset_complete.html'
    # ), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)