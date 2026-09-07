from django.urls import path

from .views import EquipoDetailView, EquipoListView


urlpatterns = [
    path("api/", EquipoListView.as_view(), name="equipos-api"),
    path(
        "<int:id_equipo>/",
        EquipoDetailView.as_view(),
        name="equipo-detail"
    ),
]