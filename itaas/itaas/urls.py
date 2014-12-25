from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


from django.conf.urls import url, include
from rest_framework import routers
from itaas.apps.aws.views import MyRESTView


#router = routers.DefaultRouter()
#router.register(r'rest_views', views.MyRESTView)
#router.register(r'groups', views.GroupViewSet)


#urlpatterns = patterns('',
#    url(r'^aws/', include('itaas.apps.aws.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#
#
#
#
#) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns = [
# #   url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]


urlpatterns = patterns('',
    # this URL passes resource_id in **kw to MyRESTView
    url(r'^api/v1.0/resource/(?P<resource_id>\d+)[/]?$', MyRESTView.as_view(), name='my_rest_view'),
    url(r'^api/v1.0/resource[/]?$', MyRESTView.as_view(), name='my_rest_view'),
)

