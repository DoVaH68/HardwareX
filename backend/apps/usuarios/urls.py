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

from .views import (
    LoginView,
    LogoutView,
    PerfilView,
    RegisterView,
)


urlpatterns = [
    # =========================
    # PÁGINA PRINCIPAL
    # =========================

    path(
        "",
        InicioPageView.as_view(),
        name="inicio",
    ),

    # =========================
    # AUTENTICACIÓN
    # =========================

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    # =========================
    # USUARIO
    # =========================

    path(
        "perfil/",
        PerfilPageView.as_view(),
        name="perfil",
    ),

    path(
        "perfil/<int:id_usuario>/",
        PerfilView.as_view(),
        name="perfil_usuario",
    ),

    # =========================
    # TÉCNICO
    # =========================

    path(
        "tecnico/",
        TecnicoPageView.as_view(),
        name="tecnico",
    ),

    path(
        "perfil-tecnico/",
        PerfilTecnicoPageView.as_view(),
        name="perfil_tecnico",
    ),

    # =========================
    # HISTORIAL
    # =========================

    path(
        "historial/",
        HistorialPageView.as_view(),
        name="historial",
    ),

    path(
        "historial-admin/",
        HistorialAdminPageView.as_view(),
        name="historial_admin",
    ),

    # =========================
    # ADMINISTRACIÓN
    # =========================

    path(
        "admin-dashboard/",
        AdminHomePageView.as_view(),
        name="admin_home",
    ),

    path(
        "tecnicos-admin/",
        TecnicosAdminPageView.as_view(),
        name="tecnicos_admin",
    ),

    path(
        "equipos-admin/",
        EquiposAdminPageView.as_view(),
        name="equipos_admin",
    ),

    # =========================
    # EQUIPOS
    # =========================

    path(
        "asignaciones/",
        AsignacionesPageView.as_view(),
        name="asignaciones",
    ),

    path(
        "equipos/",
        EquiposPageView.as_view(),
        name="equipos",
    ),

    # =========================
    # PIEZAS
    # =========================

    path(
        "piezas/",
        PiezasPageView.as_view(),
        name="piezas",
    ),

    # =========================
    # SOLICITUDES
    # =========================

    path(
        "solicitudes/",
        SolicitudesPageView.as_view(),
        name="solicitudes",
    ),

    # =========================
    # MANTENIMIENTOS
    # =========================

    path(
        "mantenimientos/",
        MantenimientosPageView.as_view(),
        name="mantenimientos",
    ),

    # =========================
    # REPORTES
    # =========================

    path(
        "reportes/",
        ReportesPageView.as_view(),
        name="reportes",
    ),

    path(
        "reportes-recientes/",
        ReportesRecientesPageView.as_view(),
        name="reportes_recientes",
    ),
]