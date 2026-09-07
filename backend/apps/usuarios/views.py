from django.contrib.auth import logout
from django.shortcuts import redirect, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Usuario
from .serializers import LoginSerializer, UsuarioSerializer
from .services import autenticar_usuario, obtener_usuario


class LoginView(APIView):

    def get(self, request):
        if request.session.get("usuario_id"):
            return redirect("inicio")

        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        clave = request.POST.get("clave")

        if not email or not clave:
            return render(
                request,
                "login.html",
                {
                    "error": "Debes ingresar correo y contraseña."
                },
            )

        usuario = autenticar_usuario(email, clave)

        if usuario is None:
            return render(
                request,
                "login.html",
                {
                    "error": "Correo o contraseña incorrectos."
                },
            )

        request.session.flush()

        request.session["usuario_id"] = usuario.id_usuario
        request.session["usuario_nombre"] = usuario.nombre_usuario
        request.session["usuario_email"] = usuario.email

        request.session.set_expiry(60 * 60 * 8)

        return redirect("inicio")


class RegisterView(APIView):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        required_fields = [
            "nombres",
            "apellidos",
            "numero_tel",
            "nombre_usuario",
            "email",
            "fecha_nacimiento",
            "clave",
        ]

        if any(
            not request.POST.get(field)
            for field in required_fields
        ):
            return render(
                request,
                "login.html",
                {
                    "error": (
                        "Todos los campos de registro "
                        "son obligatorios."
                    )
                },
            )

        if Usuario.objects.filter(
            email=request.POST.get("email")
        ).exists():
            return render(
                request,
                "login.html",
                {
                    "error": "El correo ya está registrado."
                },
            )

        if Usuario.objects.filter(
            nombre_usuario=request.POST.get("nombre_usuario")
        ).exists():
            return render(
                request,
                "login.html",
                {
                    "error": (
                        "El nombre de usuario "
                        "ya está registrado."
                    )
                },
            )

        Usuario.objects.create(
            nombres=request.POST.get("nombres"),
            apellidos=request.POST.get("apellidos"),
            numero_tel=request.POST.get("numero_tel"),
            nombre_usuario=request.POST.get("nombre_usuario"),
            email=request.POST.get("email"),
            fecha_nacimiento=request.POST.get("fecha_nacimiento"),
            clave=request.POST.get("clave"),
            id_rol_fk=1,
        )

        return redirect("login")


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return redirect("login")

    def post(self, request):
        logout(request)
        return redirect("login")


class PerfilView(APIView):

    def get(self, request, id_usuario):

        usuario = obtener_usuario(id_usuario)

        if usuario is None:
            return Response(
                {
                    "detail": "Usuario no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UsuarioSerializer(usuario)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )