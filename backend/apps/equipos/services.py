from .models import Equipo


def listar_equipos():
    return (
        Equipo.objects
        .select_related(
            "id_tipo_equipo_fk",
            "id_ubicacion_fk"
        )
        .order_by("codigo")
    )


def obtener_equipo(id_equipo):

    try:
        return (
            Equipo.objects
            .select_related(
                "id_tipo_equipo_fk",
                "id_ubicacion_fk"
            )
            .get(id_equipo=id_equipo)
        )

    except Equipo.DoesNotExist:
        return None