from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
       url(r'^recharge/$', views.recharge, name='recharge'),
    url(r'^charge/$', views.charge, name='charge'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('createastroprofile', views.createastroprofile, name='createastroprofile'),
    #path('createprofile', views.createprofile, name='createprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('updateastroprofile', views.updateastroprofile, name='updateastroprofile'),
    path('updateprofilepic', views.updateprofilepic, name='updateprofilepic'),
    path('completeprofile', views.completeprofile, name='completeprofile'),
    #path('recharge', views.recharge, name='recharge'),
    #path('charge', views.charge, name='charge'),
    path('astrosearch', views.astrosearch, name='astrosearch'),
   
   
   
]