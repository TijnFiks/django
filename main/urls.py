from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('departments/', views.departments),
    path('department/', views.new_department),
    path('employee/', views.new_employee)
]