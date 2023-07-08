"""
URL configuration for Locale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from Locale.views import RegionViewSet, StateViewSet, LGAViewSet, CityViewSet


API_DESCRIPTION = f"""
# Introduction

This is the API documentation for the **Locale API** project.
"""
schema_view = get_schema_view(
   openapi.Info(
      title="Locale API",
      default_version='v1.0.0',
      description=API_DESCRIPTION,
      contact=openapi.Contact(email="gloryonyinye13@gmail.com")
   ),
   public=True,
   permission_classes=[AllowAny],
   authentication_classes=[],
)

router = DefaultRouter()
router.register(r"regions", RegionViewSet)
router.register(r"states", StateViewSet)
router.register(r"lgas", LGAViewSet)
router.register(r"cities", CityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
