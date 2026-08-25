from django.urls import path

from .views import EquipoDetailView, EquipoListView


urlpatterns = [
    path("", EquipoListView.as_view(), name="equipos"),
    path(
        "<int:id_equipo>/",
        EquipoDetailView.as_view(),
        name="equipo-detail"
    ),
]