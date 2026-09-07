from django.urls import path

from .views import (
    ReporteDetailView,
    ReporteListView,
)


urlpatterns = [
    path(
        "api/",
        ReporteListView.as_view(),
        name="reportes-api"
    ),

    path(
        "<int:id_reporte>/",
        ReporteDetailView.as_view(),
        name="reporte-detail"
    ),
]