from django.urls import path

from trackball import views

urlpatterns = [
    path('', views.index, name='index'),
]