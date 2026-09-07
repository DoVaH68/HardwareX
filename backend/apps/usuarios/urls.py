from django.urls import path

from core.page_views import (
    AdminHomePageView,
    AsignacionesPageView,
    EquiposAdminPageView,
    EquiposPageView,
    HistorialAdminPageView,
    HistorialPageView,
    InicioPageView,
    MantenimientosPageView,
    PerfilPageView,
    PerfilTecnicoPageView,
    PiezasPageView,
    ReportesPageView,
    ReportesRecientesPageView,
    SolicitudesPageView,
    TecnicoPageView,
    TecnicosAdminPageView,
)
from .views import LoginView, PerfilView, RegisterView


urlpatterns = [
    path("", InicioPageView.as_view(), name="inicio"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("historial/", HistorialPageView.as_view(), name="historial"),
    path("perfil/", PerfilPageView.as_view(), name="perfil"),
    path("tecnico/", TecnicoPageView.as_view(), name="tecnico"),
    path(
        "perfil-tecnico/",
        PerfilTecnicoPageView.as_view(),
        name="perfil_tecnico",
    ),
    path(
        "admin-dashboard/",
        AdminHomePageView.as_view(),
        name="admin_home",
    ),
    path(
        "reportes-recientes/",
        ReportesRecientesPageView.as_view(),
        name="reportes_recientes",
    ),
    path(
        "tecnicos-admin/",
        TecnicosAdminPageView.as_view(),
        name="tecnicos_admin",
    ),
    path(
        "historial-admin/",
        HistorialAdminPageView.as_view(),
        name="historial_admin",
    ),
    path(
        "equipos-admin/",
        EquiposAdminPageView.as_view(),
        name="equipos_admin",
    ),
    path(
        "asignaciones/",
        AsignacionesPageView.as_view(),
        name="asignaciones",
    ),
    path("equipos/", EquiposPageView.as_view(), name="equipos"),
    path("piezas/", PiezasPageView.as_view(), name="piezas"),
    path(
        "solicitudes/",
        SolicitudesPageView.as_view(),
        name="solicitudes",
    ),
    path(
        "mantenimientos/",
        MantenimientosPageView.as_view(),
        name="mantenimientos",
    ),
    path("reportes/", ReportesPageView.as_view(), name="reportes"),
    path(
        "perfil/<int:id_usuario>/",
        PerfilView.as_view(),
        name="perfil"
    ),
]