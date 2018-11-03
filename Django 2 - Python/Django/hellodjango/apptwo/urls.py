from django.urls import path, register_converter

from . import views
from . import converters

register_converter(converters.TwoDigitDayConverter, 'dd')

urlpatterns = [
    path('djangorocks/', views.djangorocks),
    path('pictures/<str:category>/', views.picture_detail),
    path('pictures/<str:category>/<int:year>/', views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>/', views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>/<dd:day>/', views.picture_detail),
]
