from rest_framework import routers

from django.urls import path,include
from .api import LeadViewSet

router=routers.DefaultRouter()
router.register('api/leads',LeadViewSet)
urlpatterns = [
    path('',include(router.urls)),
]