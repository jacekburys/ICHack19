from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views import View
from PIL import Image

class BEView(View):
    def get(self, request):
        return HttpResponse("hello world")

    def post(self, request):
        if 'myImage' in request.FILES:
            print("it's here yo")
            print(request.FILES['myImage'])
            im = Image.open(request.FILES['myImage'])
            width, height = im.size
            # DO PROCESSING
            dimRes = "Width: " + str(width) + ", Height: " + str(height) + "\n"

        return HttpResponse(dimRes)
