from django.urls import path

from .views import (
    PiezaDetailView,
    PiezaListView,
    TipoPiezaListView,
)


urlpatterns = [
    path("api/", PiezaListView.as_view(), name="piezas-api"),

    path(
        "tipos/",
        TipoPiezaListView.as_view(),
        name="tipos-pieza"
    ),

    path(
        "<int:id_pieza>/",
        PiezaDetailView.as_view(),
        name="pieza-detail"
    ),
]