from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    
    # İhtiyaca göre diğer alanları ekleyebilirsiniz.

    def __str__(self):
        return f"{self.image.name}"
