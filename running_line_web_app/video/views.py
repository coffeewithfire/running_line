from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .app.app import create_video

def index(request):

    msg = str(request.GET.get("message", ""))

    create_video(msg)

    video = open("video/app/video.mp4", "rb")
    
    return FileResponse(video, content_type="video/mp4v")