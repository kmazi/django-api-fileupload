from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import FileUploadViewSet

router = SimpleRouter()
router.register(r'upload/', FileUploadViewSet, base_name="fileupload")
urlpatterns = router.urls