from django.urls import path

from trackball import views
# from users.views import dashboard

urlpatterns = [
    path('', views.index, name='index'),
    path(r"^dashboard/", views.dashboard, name="dashboard"),
]