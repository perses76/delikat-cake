from django.conf.urls.defaults import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from myproject.pub import views
#import settings

urlpatterns = patterns('',
    (r'^$', views.genericview, {'page': 'under_construction.html'}),
    (r'^index/$', views.index),
    (r'^hello/$', views.hello),
    (r'^base/$', views.base),
    (r'^decorations/$', views.decorations),
    (r'^decorations/(?P<slug>[\w|-]+)/$', views.decorationByOccasion),
    (r'^products/(?P<slug>[\w|-]+)/$', views.products),
    (r'^ourshops/$', views.genericview, {'page': 'ourshops.html'}),
    (r'^aboutus/$', views.genericview, {'page': 'aboutus.html'}),
    (r'^makeorder/$', views.makeorder),
    url(r'^mail_sent/$', views.mail_sent_confirmation, name="mail_sent_confirmation"),
)

if settings.DEVELOPE_SERVER:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)