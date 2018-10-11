from django.urls import path
from .import views

urlpatterns = [
    path('', views.project_home, name='project_home'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
]
