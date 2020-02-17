from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from account import views as acccount_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", acccount_views.IndexView.as_view(), name="index"),
    url(r"^signup/$", acccount_views.signup, name="signup"),
    url(r'^login/$', auth_views.LoginView.as_view(),{'template_name': 'core/login.html'}, name='login'),
    #this url here
    url(r'^logout/$', auth_views.LogoutView.as_view(),{'template_name': 'core/logout.html'}, name='logout'),
]
