from rest_framework import serializers

from cameras.models import Camera


class CameraUpdateSerializer(serializers.Serializer):
    current_load = serializers.IntegerField(required=True)

class CameraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [
            'url',
            'lat',
            'long',
            'mask',
            'orientation',
            'max_cap',
            'current_load',
        ]