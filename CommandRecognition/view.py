from django.http import HttpResponse
from django.shortcuts import render
import sys
import os

def hello(request):
    return render(request, 'index.html')

def save(request):
    file = request.FILES.get('wavfile')
    destination = open(os.path.join("C:\\Users\\Youyuan Zhang\\Django_projects\\CommandRecognition\\commands", "test.wav"), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    sys.path.append('../')
    os.system('py main.py')
    return HttpResponse('thank you')