from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def djangorocks(request):
    return HttpResponse("This is a Jazzy Response")


def picture_detail(request, category, year=0, month=0, day=0):
    template = loader.get_template('apptwo/pictures.html')

    picture = {
        'filename': 'mountain.jpg',
        'categories': ['color', 'landscape' ,],
    }

    context = {
        'title': "this is the picture detail",
        'category': category,
        'year': year,
        'month': month,
        'day': day,
        'picture': picture,
    }
    return HttpResponse(template.render(context, request))



