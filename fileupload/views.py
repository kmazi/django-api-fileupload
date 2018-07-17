from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from .models import FileUpload
from .serializers import FileUploadSerializer

# Create your views here.
class FileUploadViewSet(ModelViewSet):
  queryset = FileUpload.objects.all()
  serializer_class = FileUploadSerializer
  parser_class = (MultiPartParser)

