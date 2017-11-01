from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib import admin
from django.views import defaults as default_views

from crisiscleanup.calls.urls import router as calls_api_router
from crisiscleanup.calls.urls import urlpatterns as calls_urlpatterns
from .routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

admin.site.site_header = 'Calls Service Administration'

router = DefaultRouter(trailing_slash=False)
router.extend(calls_api_router)

api_urls = []
api_urls += calls_urlpatterns
api_urls += router.urls

schema_view = get_swagger_view(title='Calls Service API')

urlpatterns = [
    url(r'^', include(api_urls, namespace='api')),
    url(r'^calls-openapi', schema_view),
    url(r'^health', lambda request: HttpResponse('Healthy!'), name='health_check'),
    url(settings.ADMIN_URL, admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^400$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
