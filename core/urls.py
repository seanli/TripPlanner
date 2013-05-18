from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^facebook-login/$', 'facebook_login'),
    url(r'^logout/$', 'logout'),
    url(r'^test/$', 'test_endpoint'),
    url(r'^get_restaurants$', 'get_poi_from_address'),
)
