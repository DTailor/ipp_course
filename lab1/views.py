from annoying.decorators import render_to
from django.http import HttpResponse
from subprocess import call


@render_to('lab1/index.html')
def main(request):
    return {}


@render_to('lab1/index.html')
def task1(request):
    command = ["youtube-dl", "-f", "5", "--output", "tmp/%(title)s.%(ext)s"]
    data = request.GET
    video_url = data.get('url')
    if video_url:
        command.append(video_url)
        process = call(command)
        return HttpResponse('ok')
    return {}