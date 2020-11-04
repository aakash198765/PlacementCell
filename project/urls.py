from django.urls import path
from project import views
from django.conf.urls import url

urlpatterns=[
    path('', views.login),
    path('home', views.login, name='home'),
    url(r'^login/$',views.login1,name='login'),
    url(r'^signup/$',views.SignUp,name='SignUp'),
    url(r'^criteria/$', views.Criteria, name='Criteria'),
    url(r'^about/$', views.About, name='About'),
    url(r'^Student Registration/$', views.stdreg,name='stdreg'),
    url(r'^crt/$',views.crt,name="crt"),
    url(r'^placementcell/$',views.placementcell,name="placementcell"),
    url(r'^Register/$', views.Register, name='Register'),
    url(r'^placedstudents/$', views.placedstudents, name='placedstudents'),
    url(r'^placed/$', views.placed, name='placed'),
    url(r'^high/$', views.high, name='high'),
    url(r'^low/$', views.low, name='low'),
]