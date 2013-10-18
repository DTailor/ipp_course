from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from subprocess import call
import json


@render_to('lab1/index.html')
def main(request):
    return {}


@csrf_exempt
@render_to('lab1/task1.html')
def task1(request):
    command = ["youtube-dl", "-f", "17", "--output", "tmp/%(title)s.%(ext)s"]
    get_data = request.GET
    post_data = request.POST
    # Single video download
    video_url = get_data.get('url')
    if video_url:
        download_command = command[:]
        download_command.append(video_url)
        process = call(download_command)
        return HttpResponse('ok')

    # Batch downloading
    videos_url = post_data.get('links')
    if videos_url:
        videos_url = json.loads(videos_url)
        for video_url in videos_url['url']:
            download_command = command[:]
            download_command.append(video_url)
            process = call(download_command)
        return HttpResponse('ok')

    # Cached links
    videos_url = post_data.get('cached_links')
    if videos_url:
        results = dict()
        videos_url = json.loads(videos_url)
        for index, video_url in videos_url.iteritems():
            download_command = command[:]
            download_command.append(video_url)
            process = call(download_command)
            results[index] = True

        return HttpResponse(json.dumps(results))
    return {}


@render_to('lab1/task2.html')
def task2(request):
    return {}


@render_to('lab1/task3.html')
def task3(request):
    return {}