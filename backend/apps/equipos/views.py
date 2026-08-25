from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Equipo
from .serializers import EquipoSerializer
from .services import listar_equipos, obtener_equipo


class EquipoListView(APIView):

    def get(self, request):

        equipos = listar_equipos()

        serializer = EquipoSerializer(
            equipos,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = EquipoSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EquipoDetailView(APIView):

    def get(self, request, id_equipo):

        equipo = obtener_equipo(id_equipo)

        if equipo is None:
            return Response(
                {"detail": "Equipo no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            EquipoSerializer(equipo).data
        )