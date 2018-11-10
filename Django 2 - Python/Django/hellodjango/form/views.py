from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from appone.forms import TestForm


def thanks(request):
    return HttpResponse('Thanks, your form has been processed')


def get_form_data(request):
    if request.method == 'POST':
        print('In POST processing')
        form = TestForm(request.POST)

        if form.is_valid():
            print('name:', form.cleaned_data['name'])
            print('email:', form.cleaned_data['email'])
            print('yes_no:', form.cleaned_data['yes_no'])
            print('city:', form.cleaned_data['city'])
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = TestForm()
    return render(request, 'appone/form.html', {'form': form})
