from django.urls import path

from .views import (
    MantenimientoDetailView,
    MantenimientoListView,
)


urlpatterns = [
    path(
        "api/",
        MantenimientoListView.as_view(),
        name="mantenimientos-api"
    ),

    path(
        "<int:id_mantenimiento>/",
        MantenimientoDetailView.as_view(),
        name="mantenimiento-detail"
    ),
]