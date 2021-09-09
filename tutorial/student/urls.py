from django.urls import path
from student import views

urlpatterns = [
  path('hello-world', views.hello_world),
  path('hello-world-2', views.hello_world_v2),
]