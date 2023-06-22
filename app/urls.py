from django.urls import path

from app.views import hello, name
from . import views

urlpatterns = [
    path('',views.hello,name= 'hello'),
    path('<str:bd>',views.name,name='bio'),
]
