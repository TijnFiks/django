from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('departments/', views.departments),
    path('new_department/', views.new_department),
    path('new_employee/', views.new_employee),
    path('delete_employee/', views.delete_employee),
    path('employee/', views.employee),
    path('delete_department/', views.delete_department),
    path('department/', views.department)
]