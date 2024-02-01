# forms.py

from django import forms
from detect.models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']  # İhtiyaca göre diğer alanları ekleyebilirsiniz
