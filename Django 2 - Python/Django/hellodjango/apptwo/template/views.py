from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def djangorocks(request):
    return HttpResponse("This is a Jazzy Response")


def picture_detail(request, category, year=0, month=0, day=0):
    context = {
        'stylesheet': 'css/style.css',
        'pictures': [
            {
                'name': 'Duck',
                'filename': 'duck.jpg',
            },
            {
                'name': 'Mountain',
                'filename': 'mountain.jpg',
            },
        ],
    }
    return render(request, "apptwo/index.html", context)



