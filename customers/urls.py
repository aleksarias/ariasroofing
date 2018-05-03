from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^api/users/$', user_list.as_view(), name='user_list'),
    url(r'^api/users/(?P<pk>[0-9]+)$', user_detail.as_view(), name='user_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
