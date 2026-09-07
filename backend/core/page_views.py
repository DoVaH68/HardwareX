from django.views.generic import TemplateView


class RegisterPageView(TemplateView):
    template_name = "login.html"


class InicioPageView(TemplateView):
    template_name = "index.html"


class HistorialPageView(TemplateView):
    template_name = "historial.html"


class PerfilPageView(TemplateView):
    template_name = "perfil.html"


class TecnicoPageView(TemplateView):
    template_name = "tecnico.html"


class PerfilTecnicoPageView(TemplateView):
    template_name = "perfil_tecnico.html"


class AdminHomePageView(TemplateView):
    template_name = "admin_home.html"


class ReportesRecientesPageView(TemplateView):
    template_name = "reportes_recientes.html"


class TecnicosAdminPageView(TemplateView):
    template_name = "tecnicos_admin.html"


class HistorialAdminPageView(TemplateView):
    template_name = "historial_admin.html"


class EquiposAdminPageView(TemplateView):
    template_name = "equipos_admin.html"


class AsignacionesPageView(TemplateView):
    template_name = "asignaciones.html"


class EquiposPageView(TemplateView):
    template_name = "equipos.html"


class PiezasPageView(TemplateView):
    template_name = "piezas.html"


class SolicitudesPageView(TemplateView):
    template_name = "solicitudes.html"


class MantenimientosPageView(TemplateView):
    template_name = "mantenimientos.html"


class ReportesPageView(TemplateView):
    template_name = "reportes.html"