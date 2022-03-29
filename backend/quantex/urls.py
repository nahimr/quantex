from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'instruments', views.InstrumentViewSet)

urlpatterns = [
    path('quantex/', include(router.urls)),
]
