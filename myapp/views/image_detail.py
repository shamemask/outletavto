import os

from django.shortcuts import render


def image_detail(request, image_name):
    image_names = os.listdir('./images')
    image_names = [x.replace('.png','') for x in image_names if x.endswith('.png')]
    return render(request, 'image_detail.html', {'image_name': image_name, 'image_names': image_names})
