from django.urls import path
from .views import add_student, list_students

urlpatterns = [
    path('add_student/', add_student, name='add_student'),
    path('list_students/', list_students, name='list_students'),
]
