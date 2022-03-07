from django.urls import path
from . import views

urlpatterns = [
    path('api/instrument', views.InstrumentListCreate.as_view({'get': list})),
]