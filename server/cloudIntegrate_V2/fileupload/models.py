from django.db import models
from django.utils.timezone import now

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# New model for metadata
class FileUploadMetadata(models.Model):
    datetime_of_creation = models.DateTimeField(default=now)  # Timestamp
    ip_address = models.GenericIPAddressField()              # IP Address
    port_no = models.IntegerField()                          # Port number
    zip_file_name = models.CharField(max_length=255)         # File name

    def __str__(self):
        return f"{self.zip_file_name} from {self.ip_address}:{self.port_no}"