import io

from rest_framework.test import APITestCase
from django.conf import settings
from urllib.parse import urlparse
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from .models import FileUpload

# Create your tests here.
class FileUploadTests(APITestCase):
  def tearDown(self):
    FileUpload.objects.all().delete()

  def _create_test_image(self):
    file = io.BytesIO()
    image = Image.new('RGB', (50, 50), color=(30, 40, 3))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file

  def test_upload_files(self):
    data = dict()
    data.update(data_file=self._create_test_image(), first_name="touchstone", last_name="mazimia",
      referrer="celestine")
    url = reverse('fileupload-list')
    response = self.client.post(url, data, format='multipart')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    touchstone = FileUpload.objects.get(first_name="touchstone")
    self.assertTrue(touchstone)
