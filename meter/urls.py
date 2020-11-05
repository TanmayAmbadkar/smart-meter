from django.urls import include, path
from rest_framework import routers
from meter.views import *

router = routers.DefaultRouter()
router.register('meter', MeterViewSet)
router.register('reading', ReadingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('update/', AddReading.as_view(), name='update'),
]
