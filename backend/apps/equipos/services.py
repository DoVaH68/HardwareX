from .models import Equipo


def listar_equipos():
    return Equipo.objects.all()


def obtener_equipo(id_equipo):
    try:
        return Equipo.objects.get(id_equipo=id_equipo)
    except Equipo.DoesNotExist:
        return None