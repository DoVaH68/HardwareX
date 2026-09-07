from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, render

from .serializers import UsuarioSerializer, LoginSerializer
from .models import Usuario
from .services import autenticar_usuario, obtener_usuario


class LoginView(APIView):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.validated_data["email"]
        clave = serializer.validated_data["clave"]

        usuario = autenticar_usuario(email, clave)

        if usuario is None:
            return Response(
                {
                    "detail": "Correo o contraseña incorrectos."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                "message": "Inicio de sesión exitoso.",
                "usuario": UsuarioSerializer(usuario).data
            },
            status=status.HTTP_200_OK
        )


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

        if any(not request.data.get(field) for field in required_fields):
            return render(
                request,
                "login.html",
                {"error": "Todos los campos de registro son obligatorios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Usuario.objects.create(
            nombres=request.data["nombres"],
            apellidos=request.data["apellidos"],
            numero_tel=request.data["numero_tel"],
            nombre_usuario=request.data["nombre_usuario"],
            email=request.data["email"],
            fecha_nacimiento=request.data["fecha_nacimiento"],
            clave=request.data["clave"],
            id_rol_fk=1,
        )

        return redirect("login")


class PerfilView(APIView):

    def get(self, request, id_usuario):

        usuario = obtener_usuario(id_usuario)

        if usuario is None:
            return Response(
                {
                    "detail": "Usuario no encontrado."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsuarioSerializer(usuario)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )