"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
# from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



API_DESCRIPTION = 'A web API for basic twitter functionalities'
# schema_view = get_swagger_view(title='FleetWeet API')
# schema_view = get_schema_view(title='FleetWeet API')

schema_view = get_schema_view(
   openapi.Info(
      title="FleetWeet API",
      default_version='v1',
      description=API_DESCRIPTION,
      terms_of_service="https://www.fleetweet.com/policies/terms/",
      contact=openapi.Contact(email="contact@fleetweet.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/registration/', include('dj_rest_auth.registration.urls'), name='register'),
    # path('swagger-docs/', schema_view),
    # path('swagger-docs/', schema_view),
    path('docs/', include_docs_urls(title='FleetWeet Api', description=API_DESCRIPTION)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)