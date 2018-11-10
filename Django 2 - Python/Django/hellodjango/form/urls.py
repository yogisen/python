from django.contrib import admin
from django.urls import path, include

from appone import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', views.thanks, name='thanks'),
    path('getformdata/', views.get_form_data, name='get-form-data'),
]
