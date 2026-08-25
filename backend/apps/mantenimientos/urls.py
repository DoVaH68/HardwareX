from django.urls import path

from .views import (
    MantenimientoDetailView,
    MantenimientoListView,
)


urlpatterns = [
    path(
        "",
        MantenimientoListView.as_view(),
        name="mantenimientos"
    ),

    path(
        "<int:id_mantenimiento>/",
        MantenimientoDetailView.as_view(),
        name="mantenimiento-detail"
    ),
]