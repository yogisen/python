from django.shortcuts import render
from peoplebook.peoples import people


# Create your views here.
def users_list(request, display='small'):
    context = {
        'users': people,
        'display': display,
    }
    return render(request, 'peoplebook/users_list.html', context)


def users_detail(request, name):
    context = {
        'user': people[name],
    }
    return render(request, 'peoplebook/users_detail.html', context)
