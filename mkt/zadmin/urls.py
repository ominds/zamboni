from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url('^ecosystem$', views.ecosystem, name='mkt.zadmin.ecosystem'),
    # Featured apps selector.
    url('^apps/featured$', views.featured_apps_admin,
        name='zadmin.featured_apps'),
    url('^apps/featured_ajax$', views.featured_apps_ajax,
        name='zadmin.featured_apps_ajax'),
    url('^apps/featured_categories_ajax$', views.featured_categories_ajax,
        name='zadmin.featured_categories_ajax'),
    url('^apps/set_region_ajax$', views.set_region_ajax,
        name='zadmin.set_region_ajax'),
)
