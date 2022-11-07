from django.urls import path, re_path


from api.views import UpdateCamera, GetCamerasData, GetCameraMask

urlpatterns = [
    path('cameras/<int:camera_id>/', UpdateCamera.as_view(), name='update-camera'),
    path('cameras/<int:camera_id>/mask/', GetCameraMask.as_view(), name='get-camera-mask'),

    path('cameras/get-data/', GetCamerasData.as_view(), name='cameras-data')
]