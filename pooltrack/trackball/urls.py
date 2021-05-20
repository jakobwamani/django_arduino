from django.urls import path,include
from trackball import views
# from users.views import dashboard

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name="dashboard"),
	path('accounts/', include("django.contrib.auth.urls")),
	path('register/', views.register, name="register"),
]