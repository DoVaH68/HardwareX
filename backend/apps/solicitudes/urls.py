from django.urls import path

from .views import (
    SolicitudDetailView,
    SolicitudListView,
)


urlpatterns = [
    path(
        "api/",
        SolicitudListView.as_view(),
        name="solicitudes-api"
    ),

    path(
        "<int:id_solicitud>/",
        SolicitudDetailView.as_view(),
        name="solicitud-detail"
    ),
]