from rest_framework.routers import DefaultRouter
from flightservices import views
from eip import views as eipViews
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.decorators import api_view
from django.contrib import admin
from django.urls import path, include
#from rest_framework.response import Response
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Flights API')


router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)
router.register('idenities', eipViews.IdentityViewSet)
router.register('employees', eipViews.EmployeeViewSet)
router.register('timestamps', eipViews.TimeStampViewSet)


@api_view(('GET',))
def hello_me(request):
    me = {
        "name": "Malama",
        "age": 31,
        "sal": 1000
    }

    #return Response(me)
    return JsonResponse(me)

@api_view(('POST',))
def userprofile(data):
    dataX = data;

    return JsonResponse(dataX)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs',),
    path('api/hello/', hello_me),
    path('swagger', schema_view),
    path('flightServices/', include(router.urls)),
    path('eip/', include(router.urls)),
    path('userprofile', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static (
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT,
    )