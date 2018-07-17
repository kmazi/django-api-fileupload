from django.db import models

# Create your models here.
class FileUpload(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  referrer = models.CharField(max_length=100)
  data_file = models.FileField(upload_to='uploads/%y/%m')

  objects = models.Manager()

  def __str__(self):
    return self.first_name
  