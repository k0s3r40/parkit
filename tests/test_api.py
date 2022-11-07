from django.test import TestCase
from django.urls import reverse

from cameras.models import Camera


class ApiTestCase(TestCase):
    fixtures = ['./tests/cameras_fixture.json']

    def test_update_camera(self):
        url = reverse('update-camera', kwargs=dict(camera_id=1))
        request_body = {
            'current_load': 30
        }
        self.client.post(url, data=request_body, content_type='application/json')
        self.assertEqual(Camera.objects.get(id=1).current_load, 30)

    def test_get_camera_mask(self):
        url = reverse('get-camera-mask', kwargs=dict(camera_id=1))
        response = self.client.get(url)
        print(url)
        print(response.json())

    def test_get_cameras(self):
        url = reverse('cameras-data')
        response = self.client.get(url)
        print(response.json())