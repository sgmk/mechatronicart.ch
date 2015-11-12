from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from tastypie.api import Api
#from projects.api import ProjectResource

from django.views.generic import TemplateView

admin.autodiscover()

v1_api = Api(api_name=settings.API_VERSION)
#v1_api.register(ProjectResource())


urlpatterns = patterns(
    '',

    #url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),

    #(r'^api/', include(v1_api.urls)),

    ('^markdown/', include( 'django_markdown.urls')),

    (r'^admin/', include(admin.site.urls)),

    (r'^newsletter/', include('newsletter.urls')),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
