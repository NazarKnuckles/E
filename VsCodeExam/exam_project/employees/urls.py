from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.health_check, name='ping'),
    path('', views.employee_list, name='employee_list'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/update/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
