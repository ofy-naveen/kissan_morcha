

# Create your models here.
from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
