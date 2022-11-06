from django.urls import path, re_path


from api.views import UpdateCamera, GetCamerasData

urlpatterns = [
    path('cameras/<int:camera_id>/', UpdateCamera.as_view(), name='update-camera'),
    path('cameras/get-data/', GetCamerasData.as_view(), name='cameras-data')
]