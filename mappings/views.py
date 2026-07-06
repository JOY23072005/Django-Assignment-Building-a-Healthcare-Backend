from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(
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


class PatientDoctorsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):

        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id
        )

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True
        )

        return Response(serializer.data)


class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):

        try:
            mapping = PatientDoctorMapping.objects.get(pk=pk)

        except PatientDoctorMapping.DoesNotExist:

            return Response(
                {"error": "Mapping not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        mapping.delete()

        return Response(
            {"message": "Mapping deleted successfully."},
            status=status.HTTP_200_OK
        )