from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # name parameter allows dynamic insertion of the path into template
    path('room/<str:pk>', views.room, name='room')
]
