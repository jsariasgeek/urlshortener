import json
import threading
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from urls.async_tasks import update_url_title

from urls.models import URL

# Create your views here.
@require_http_methods(["GET", "POST"])
@csrf_exempt
def short_url(request):
    if request.method == "GET":
        # return the template
        return render(request, 'short_url.html')
    param_dict = json.loads(request.body)
    url = param_dict.get('url')
    if not url:
        return HttpResponse({
            "error":"url is required"
        }, status=400)
    # if url already exists, return the shorted url
    url_instance = URL.objects.get_or_create(full_url=url)[0]

    # in a separate thread, update the title of the url
    task_thread = threading.Thread(target=update_url_title, args=(url_instance,))
    task_thread.start()

    return HttpResponse(json.dumps({
        "url": url,
        "shorted_url":url_instance.shorted_url,
    }), content_type="application/json", status=201)


@require_http_methods(["GET"])
def redirect_url(request):
    # check if the url is a shorted url
    key = request.path.replace("/", "")
    url_instance = get_object_or_404(URL, key=key) # get the url instance or return 404
    url_instance.access_counter += 1 # update the access counter
    url_instance.save() # save the changes
    return redirect(url_instance.full_url)


@require_http_methods(["GET"])
def top_100_most_accessed_urls(request):
    urls = URL.objects.order_by('-access_counter')[:100]
    if request.GET.get('format') == 'html':
        return render(request, 'top_100.html', {'urls': urls})
    return HttpResponse(json.dumps({
        "urls": [url.as_dict() for url in urls]
    }), content_type="application/json")


def home(request):
    return render(request, 'home.html')