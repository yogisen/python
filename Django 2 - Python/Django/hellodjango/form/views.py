from django.shortcuts import render

from appone.forms import TestForm

def get_form_data(request):
    form = TestForm()
    return render(request, 'appone/form.html', {'form': form})
