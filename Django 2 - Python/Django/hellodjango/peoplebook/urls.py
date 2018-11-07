from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users_list),
    path('users/<str:display>/', views.users_list),
    path('users/<str:name>/detail/', views.users_detail, name='peoplebook-users-detail'),
]
