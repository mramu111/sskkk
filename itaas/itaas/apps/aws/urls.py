#from itaas.apps.aws.views import MyRESTView

from itaas.apps.aws import views
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # this URL passes resource_id in **kw to MyRESTView
    #url(r'^api/v1.0/resource/(?P<resource_id>\d+)[/]?$', login_required(MyRESTView.as_view()), name='my_rest_view'),
    #url(r'^api/v1.0/resource[/]?$', login_required(MyRESTView.as_view()), name='my_rest_view'),

    url(r'^api/v1.0/resource/(?P<resource_id>\d+)[/]?$', views.MyRESTView.as_view(), name='my_rest_view'),
    url(r'^api/v1.0/resource[/]?$', views.MyRESTView.as_view(), name='my_rest_view'),

    #url(r'^api/register/$', 'auth.views.register'),
    url(r'^api/login/$', 'itaas.apps.aws.views.login'),

    url(r'^api/logout/$', views.logout),
)
