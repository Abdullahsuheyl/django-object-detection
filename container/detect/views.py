# views.py

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
import cv2
from ultralytics import YOLO
from .models import UploadedImage
import os

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Başka bir sayfaya yönlendirme yapabilirsiniz
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')


def detect_objects(request):
    class_names = {0: 'human'}
    model = YOLO("detect/son.pt")
    uploaded_image = UploadedImage.objects.latest('id')
    image_path = uploaded_image.image.path

    image = cv2.imread(image_path)
    detections = model(image)[0]
    for detection in detections.boxes.data.tolist():
        x1, y1, x2, y2, score, ID = detection
        if score >= 0.2:
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            
            color = (0, 255, 0)  # Yeşil renk
            thickness = 2
            
            cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        
            if int(ID) in class_names:
                class_name = class_names[int(ID)]
            else:
                class_name = 'Unknown'
                
            
            text = f"{class_name},{score:.2f}"
            text_position = (x1+50, y1) 
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            font_color = (0, 255, 0)  
            font_thickness = 1
            
            
            cv2.putText(image, text, text_position, font, font_scale, font_color, font_thickness)
    result_image_path = os.path.join("media", "result", "result.jpg")
    cv2.imwrite(result_image_path, image)
    context = {'uploaded_image': uploaded_image, 'result_image_path': "/media/result/result.jpg"}
    return render(request, 'detect_objects.html', context)