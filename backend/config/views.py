from django.shortcuts import render


def inicio(request):
    return render(request, "index.html")


def login_page(request):
    return render(request, "login.html")


def historial(request):
    return render(request, "historial.html")


def historial_admin(request):
    return render(request, "historial_admin.html")


def equipos(request):
    return render(request, "equipos.html")


def equipos_admin(request):
    return render(request, "equipos_admin.html")


def mantenimientos(request):
    return render(request, "mantenimientos.html")


def perfil(request):
    return render(request, "perfil.html")


def perfil_tecnico(request):
    return render(request, "perfil_tecnico.html")


def piezas(request):
    return render(request, "piezas.html")


def reportes(request):
    return render(request, "reportes.html")


def reportes_recientes(request):
    return render(request, "reportes_recientes.html")


def solicitudes(request):
    return render(request, "solicitudes.html")


def tecnico(request):
    return render(request, "tecnico.html")


def tecnicos_admin(request):
    return render(request, "tecnicos_admin.html")


def asignaciones(request):
    return render(request, "asignaciones.html")


def admin_home(request):
    return render(request, "admin_home.html")


def crear_solicitud(request):
    return render(request, "crear_solicitud.html")