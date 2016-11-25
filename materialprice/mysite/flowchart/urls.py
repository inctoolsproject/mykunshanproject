from django.conf.urls import url, include

from . import views

app_name = 'flowchart'
urlpatterns = [
    # url(r'^style19/$', views.style19, name='style19'),
    # url(r'^bydate/(?P<setnum>[0-9]+)/$', views.bydate, name='bydate'),
    # url(r'^vacation', views.vacation, name='vacation'),
    # url(r'^list', views.view_flowchart_list, name='view_flowchart_list'),
    # url(r'^v2', views.indexv2, name='indexv2'),
    # url(r'^$', views.index, name='index'),
    # url(r'^receiving', views.receiving, name='receiving'),
    # url(r'^smm', views.smm, name='smm'),
    # url(r'^po', views.po, name='po'),
    url(r'^flowchart/$', views.view_flowchart_list, name='view_flowchart_list'),
    url(r'^flowchart/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.view_flowchart, name='view_flowchart'), #item001/123 後面有東西都好
    # url(r'^', views.index, name='index'),

# url(r'^style19/(?P<setnum>[0-9]+)/(?P<movenum>[0-9]+)', views.style19detail2, name='style19detail2'),


]
