""" PlantegrA URL Configuration """
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from plantegra_crm import views as crm_views
from plantegra_resources import views as res_views
from plantegra_staff import views as staff_views

router = routers.DefaultRouter()
router.register(r'users', crm_views.UserViewSet)
router.register(r'customers', crm_views.CustomerViewSet)
router.register(r'appointments', crm_views.AppointmentViewSet)
router.register(r'addresses', crm_views.AddressViewSet)
router.register(r'taskforces', crm_views.TaskForceViewSet)
router.register(r'vehicles', res_views.VehicleViewSet)
router.register(r'employees', staff_views.EmployeeViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="PlantegrA API",
        default_version='v1',
        description="The full data access and manipulation API for the PlantegrA CRM/RMS/HR",
        terms_of_service="You are not allowed to use this service.",
        contact=openapi.Contact(email="jonas@integra-lahr.de"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
