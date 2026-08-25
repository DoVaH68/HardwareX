from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("apps.usuarios.urls")),

    path("equipos/", include("apps.equipos.urls")),

    path("piezas/", include("apps.piezas.urls")),

    path("solicitudes/", include("apps.solicitudes.urls")),

    path("mantenimientos/", include("apps.mantenimientos.urls")),

    path("reportes/", include("apps.reportes.urls")),
]