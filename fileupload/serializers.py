from rest_framework import serializers
from .models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
  serializers.SlugRelatedField(slug_field='id', read_only=True)
  class Meta():
    model = FileUpload
    fields = ('first_name', 'last_name', 'referrer', 'data_file')