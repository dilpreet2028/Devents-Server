from django.conf.urls import include, url
from . import views

urlpatterns =[
    url(r'^login/$',views.LoginView.as_view(),name="Login"),
    url(r'^gcm_reg/$',views.GCMView.as_view(),name="GCM reg"),


]
