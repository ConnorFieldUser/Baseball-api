"""Baseball_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from BaseballStats.views import MasterListCreateAPIView, MasterDetailUpdateDestroyAPIView, Batting_recordListCreateAPIView, Batting_recordDetailUpdateDestroyAPIView, Pitching_recordListCreateAPIView, Pitching_recordDetailUpdateDestroyAPIView, Fielding_recordListCreateAPIView, SpecialDetailUpdateDestroyAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # API Views
    url(r'^master/$', MasterListCreateAPIView.as_view(), name="master_list_create_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', MasterDetailUpdateDestroyAPIView.as_view(), name="master_detail_update_destroy_api_view"),

    url(r'^batting/$', Batting_recordListCreateAPIView.as_view(), name="batting_record_list_create_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', Batting_recordDetailUpdateDestroyAPIView.as_view(), name="batting_record_detail_update_destroy_api_view"),

    url(r'^pitching/$', Pitching_recordListCreateAPIView.as_view(), name="pitching_list_create_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', Pitching_recordDetailUpdateDestroyAPIView.as_view(), name="pitching_record_detail_update_destroy_api_view"),

    url(r'^fielding/$', Fielding_recordListCreateAPIView.as_view(), name="fielding_list_create_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', SpecialDetailUpdateDestroyAPIView.as_view(), name="special_detail_update_destroy_api_view")

]
