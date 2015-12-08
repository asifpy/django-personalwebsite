from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

from myprofile.web.views import(
    WebsiteView,
    PythonHubView
)


urlpatterns = [

    url(r'^$', WebsiteView.as_view()),
    url(r'^pythonhub/$', PythonHubView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
]

urlpatterns += patterns(
    '',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
)
