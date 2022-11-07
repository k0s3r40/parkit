import base64

from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CameraUpdateSerializer, CameraInfoSerializer, CameraMaskSerializer
from cameras.models import Camera


class UpdateCamera(APIView):
    serializer_class = CameraUpdateSerializer

    def post(self, request, camera_id):
        camera = get_object_or_404(Camera, id=camera_id)
        serializer = CameraUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        camera.current_load = serializer.validated_data.get('current_load', camera.current_load)
        camera.save(update_fields=['current_load'])
        return Response({'current_load': camera.current_load}, status=200)


class GetCameraMask(APIView):
    serializer_class =CameraMaskSerializer
    def get(self, request, camera_id):
        camera = get_object_or_404(Camera, id=camera_id)
        serializer = self.serializer_class(data = {'mask':base64.b64encode(camera.mask.read()).decode()})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 200)

class GetCamerasData(APIView):
    serializer_class = CameraInfoSerializer
    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(Camera.objects.all(), many=True).data, status=200)
