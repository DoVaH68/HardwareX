from .models import Usuario


def autenticar_usuario(email, clave):
    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None

    if usuario.clave != clave:
        return None

    return usuario


def obtener_usuario(id_usuario):
    try:
        return Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return None