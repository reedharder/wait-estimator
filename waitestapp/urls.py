from django.conf.urls import patterns, url
from waitestapp import views

urlpatterns = patterns('',
    url(r'^1/$', views.waitapp_capacity, name='capacity'),
    url(r'^2/$', views.waitapp_aff, name='capacity'),
    url(r'^3/$', views.waitapp_attr, name='attributes'),
    url(r'^4/$', views.waitapp_contrule, name='contrules'),
    url(r'^5/$', views.waitapp_delrule, name='delrules'),
    url(r'^6/$', views.waitapp_utilization, name='utilization'),
    url(r'^results/$', views.waitapp_results, name='results'),
    url(r'^$', views.home_view, name='home'),
    
)

