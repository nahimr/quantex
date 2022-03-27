from django.urls import path
from . import views

urlpatterns = [
    path('api/instrument', views.InstrumentViewSet.as_view({'get': list})),
]